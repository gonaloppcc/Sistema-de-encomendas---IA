import logging
from math import inf

from algoritmos_procura.common import calcula_distancia, caminho_to_string
from algoritmos_procura.common import maximo_peso_uma_viagem
from base_conhecimento.Estafeta import Estafeta
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, origens
from base_conhecimento.circuitos import adiciona_circuito
from gera_encomendas.Entrega import Entrega
# Entregas realizadas
from gera_encomendas.gera_caminhos import descobre_possiveis_caminhos


def encomenda_valida(encomenda_id: int):
    """
    Indica se uma encomenda é válida. Para isso, não pode ter sido entregue, e o seu peso não deve ultrapassar a
    capacidade de todos os veículos disponíveis.
    @param encomenda_id: Id da encomenda analisada.
    @return: Se é válida ou não.
    """
    # O máximo possível é o peso que o veículo com maior carga pode transportar.
    maximo_possivel = maximo_peso_uma_viagem()
    return (not Entrega.encomenda_entregue(encomenda_id)) and encomendas.get(encomenda_id).peso <= maximo_possivel


def entregas_do_estafeta_por_dia(estafeta: int):
    """
    Descobre todas as encomendas que um dado estafeta deve fazer por dia, pelas atribuições da base de conhecimento.
    No entanto, verificamos se a encomenda não foi já entregue. Também verifica se é possível entregar a encomenda,
    com os veículos disponibilizados. @param estafeta: ‘id’ do estafeta @return: Lista de id's das encomendas que o
    estafeta deve entregar por dia deve entregar.
    """
    lista_encomendas_por_data = {}

    for atribuicao in atribuicoes:
        estafeta_id = atribuicao.estafeta_id
        encomenda_id = atribuicao.encomenda_id
        if estafeta_id == estafeta and encomenda_valida(encomenda_id):
            data_encomenda = encomendas.get(encomenda_id).data_encomenda
            lista_encomendas_por_data.setdefault(data_encomenda, []).append(encomenda_id)

    return lista_encomendas_por_data.values()


def possivel_por_pesos(um_caminho_possivel):
    """
    Verifica se é possível fazer o circuito associado a uma lista de encomendas. Recebemos algo do tipo:
    [[(local1, id_encomenda1) , (local2, id_encomenda2)], [(local3, id_encomenda13]].
    Cada lista do argumento representa um circuito, descrito pelos pontos de entrega, e as entregas para realizar.
    Se a soma do peso das encomendas desse circuito ultrapassar o máximo, dizemos que esse circuito não é possível
    @param um_caminho_possivel: Lista de circuitos e respetivos ids de encomendas entregues.
    @return: Se é possível ou não realizar esse percurso.
    """
    # O máximo possível é o peso que o veículo com maior carga pode transportar.
    maximo_possivel = maximo_peso_uma_viagem()

    for circuito in um_caminho_possivel:
        carga_atual = 0
        for cam, enc_id in circuito:
            carga_atual += encomendas.get(enc_id).peso
        if carga_atual > maximo_possivel:
            logging.debug("Este percurso não consegue entregar as encomendas")
            return False
    return True


def melhor_caminho_descoberto(estafeta_id, melhor_caminho):
    """
    Função que descobre quais os circuitos que estão no melhor caminho.
    @param estafeta_id: Usado para guardar o circuito corretamente.
    @param melhor_caminho: Melhor caminho usado para entregar as encomendas do estafeta.
    """
    logging.info("Melhor caminho foi calculado.")
    # Precisamos de juntar os caminhos num circuito, isto é, um conjunto de caminhos que sai e volta à base.
    # Este circuito pode entregar uma ou mais encomendas.
    circuito_atual = []
    # Também queremos saber que encomendas foram entregues nesse circuito
    encomendas_entregues_neste_circuito = []
    # Para não introduzirmos paragens repetidas, porque se entregarmos duas encomendas no mesmo local, esse local aparece em duplicado.
    ultimo_local = None
    for sub_percurso_atual in range(0, len(melhor_caminho)):
        # Primeiro, vamos ver que encomendas serão entregues nessa viagem

        caminho, enc_id = melhor_caminho[sub_percurso_atual]
        # Junta os vários caminhos, entre várias paragens Porque até aqui tínhamos os caminhos da base à
        # entrega1, da entrega1 à entrega2, e de volta à base, cada um numa lista separada. Agora queremos juntar
        # tudo.
        for paragem in caminho:
            if paragem != ultimo_local:
                circuito_atual.append(paragem)
                ultimo_local = paragem
        if enc_id == -1:
            # print("Quero a cidade origem: ", paragem.nome)
            adiciona_circuito(circuito_atual, encomendas_entregues_neste_circuito, estafeta_id)
            circuito_atual.clear()
            # Temos de voltar a adicionar a cidade de origem.
            circuito_atual.append(paragem)
            encomendas_entregues_neste_circuito.clear()
        else:
            encomendas_entregues_neste_circuito.append(enc_id)


def gera_circuito_um_estafeta(estafeta_id, algoritmo, cidade):
    """
    Gera as entregas de um dado estafeta. Recebe o algoritmo usado para o cálculo dos caminhos.
    @param estafeta_id: Estafeta que queremos analisar.
    @param algoritmo: Qual o algoritmo a usar para gerar os percursos entre paragens.
    @param cidade: Cidade onde a entrega ocorre.

    """
    estafeta = estafetas.get(cidade)
    logging.info(f"Vamos analisar o estafeta nr.: {estafeta_id}")
    # Lista de encomendas que o estafeta vai entregar, por dia.
    encomendas_id = entregas_do_estafeta_por_dia(estafeta_id)
    if len(encomendas_id) == 0:
        logging.info(f"O estafeta com id {estafeta_id} não tem encomendas atribuídas, ou já foram entregues.")
        return
    for encomendas_um_dia in encomendas_id:
        gera_circuitos_um_dia(algoritmo, encomendas_um_dia, estafeta, cidade)


def gera_circuitos_um_dia(algoritmo, encomendas_id: [int], estafeta: Estafeta, cidade_str: str):
    """
    Gera as entregas de um dado estafeta para um dia.
    @param algoritmo: Algoritmo utilizado para escolher caminhos entre dois locais.
    @param encomendas_id: Lista de encomendas que tem de entregar num dia.
    @param estafeta: Estafeta que realiza as entregas.
    @param cidade_str: Cidade onde a entrega ocorre.
    """
    # Combinações dos possíveis caminhos que o estafeta pode usar.
    possiveis_percursos = descobre_possiveis_caminhos(encomendas_id)

    # Guardam as melhores distâncias e caminhos
    melhor_distancia = float(inf)
    # Guarda os caminhos do melhor
    melhor_caminho = []
    # um caminho possível = [[A, B, C], [D]]
    for um_caminho_possivel in possiveis_percursos:

        if possivel_por_pesos(um_caminho_possivel):
            total_este_caminho = 0
            # Guarda os percursos que faz para entregar as várias encomendas
            caminhos_pos_algoritmos = []
            for sub_caminho in um_caminho_possivel:
                # [A, B, C]
                for atual in range(0, len(sub_caminho)):
                    # Se for a primeira paragem, tem de sair da base
                    if atual == 0:
                        (id_local, enc_id) = sub_caminho[atual]
                        local = Local.encontra_local(id_local)
                        cam = algoritmo(origens.get(cidade_str), local)
                        logging.debug("Foi analisado o caminho: ")
                        logging.debug(caminho_to_string(cam))
                        caminhos_pos_algoritmos.append((cam, enc_id))
                        total_este_caminho += calcula_distancia(cam)
                    else:
                        # Liga as outras duas paragens
                        (id_local1, enc_id1) = sub_caminho[atual - 1]
                        (id_local2, enc_id2) = sub_caminho[atual]

                        local1 = Local.encontra_local(id_local1)
                        local2 = Local.encontra_local(id_local2)

                        cam = algoritmo(local1, local2)
                        logging.debug("Foi analisado o caminho: ")
                        logging.debug(caminho_to_string(cam))
                        caminhos_pos_algoritmos.append((cam, enc_id2))
                        total_este_caminho += calcula_distancia(cam)

                # Tem de voltar à base
                (id_local1, enc_id1) = sub_caminho[atual]
                local1 = Local.encontra_local(id_local1)
                cam = algoritmo(local1, origens.get(cidade_str))
                logging.debug("Foi analisado o caminho: ")
                logging.debug(caminho_to_string(cam))
                total_este_caminho += calcula_distancia(cam)
                logging.debug(f"Este caminho tem o custo total de: {total_este_caminho}")
                caminhos_pos_algoritmos.append((cam, -1))
            logging.debug("<---------Fim de análise de um caminho------->")
            if total_este_caminho < melhor_distancia:
                logging.debug(f"Altera caminho para um melhor, {total_este_caminho}")
                # Guarda as informações do melhor caminho
                melhor_distancia = total_este_caminho
                melhor_caminho.clear()
                melhor_caminho = caminhos_pos_algoritmos.copy()
    # Nenhum caminho é possível, pode ser porque a encomenda é muito pesada
    # Ou duas, ou mais, entregas dum nodo ultrapassa o máximo.
    if melhor_distancia == float(inf):
        logging.info("Nenhuma encomenda foi entregue.")
    else:
        melhor_caminho_descoberto(estafeta.estafeta_id, melhor_caminho)


# Gera todos os circuitos.
def gerar_circuitos(algoritmo):
    """
    Gera todos os circuitos baseando-se nas atribuições.
    @param algoritmo: Algoritmo usado para descobrir o caminho entre dois pontos.
    """
    lista_estafetas = []
    for atribuicao in atribuicoes:
        cidade_encomenda = encomendas.get(atribuicao.encomenda_id).cidade_encomenda()
        lista_estafetas.append((atribuicao.estafeta_id, cidade_encomenda))
    for (estafeta_id, cidade) in lista_estafetas:
        gera_circuito_um_estafeta(estafeta_id, algoritmo, cidade)
