import logging
from math import inf


from Fase2.algoritmos_procura.common import maximo_peso_uma_viagem, calcula_distancia, caminho_to_string
from Fase2.base_conhecimento.baseConhecimento import encomendas, atribuicoes, estafetas, origens

# TODO: Passar isto para metodos de instancia da classe Entrega?
from Fase2.base_conhecimento.circuitos import adiciona_circuito
from Fase2.gera_encomendas.Entrega import Entrega
from Fase2.gera_encomendas.gera_caminhos import descobre_possiveis_caminhos


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



def entregas_do_estafeta(estafeta: int):
    """
    Descobre todas as encomendas que um dado estafeta deve fazer, pelas atribuições da base de conhecimento. No
    entanto,verificamos se a encomenda não foi já entregue. Também verifica se é possível entregar a encomenda,
    com os veículos disponibilizados. @param estafeta: Id do estafeta @return: Id's das encomendas que o estafeta
    deve entregar.
    """
    list_encomendas = []

    for atribuicao in atribuicoes:
        estafeta_id = atribuicao.estafeta_id
        encomenda_id = atribuicao.encomenda_id
        if estafeta_id == estafeta and encomenda_valida(encomenda_id):
            list_encomendas.append(encomenda_id)
    return list_encomendas


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


def gera_entrega_um_estafeta(estafeta_id, algoritmo):
    """
    Gera as entregas de um dado estafeta. Recebe o algoritmo usado para o cálculo dos caminhos.
    @param estafeta_id: Estefeta que queremos analisar.
    @param algoritmo: Qual o algoritmo a usar para gerar os percursos entre paragens.
    """
    estafeta = estafetas.get(estafeta_id)
    logging.info(f"Vamos analisar o estafeta nr.: {estafeta_id}")
    # Encomendas que o estafeta vai entregar.
    encomendas_id = entregas_do_estafeta(estafeta_id)
    if len(encomendas_id) == 0:
        logging.info(f"O estafeta com id {estafeta_id} não tem encomendas atribuídas, ou já foram entregues.")
        return
    # Combinações dos possíveis caminhos que o estafeta pode usar.
    possiveis_percursos = descobre_possiveis_caminhos(encomendas_id)
    # Local do centro de entregas, ele tem de partir e voltar para lá
    origem_cidade = origens.get(estafeta.cidade)

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
                logging.debug("[gera entrega um estafeta1] Um sub caminho é: ")
                for (local, _) in sub_caminho: logging.debug(f"{local.nome}")
                for atual in range(0, len(sub_caminho)):
                    # Se for a primeira paragem, tem de sair da base
                    if atual == 0:
                        (local, enc_id) = sub_caminho[atual]
                        cam = algoritmo(origem_cidade, local)
                        logging.debug("Foi analisado o caminho: ")
                        logging.debug(caminho_to_string(cam))
                        caminhos_pos_algoritmos.append((cam, enc_id))
                        total_este_caminho += calcula_distancia(cam)
                    else:
                        # Liga as outras duas paragens
                        (local1, enc_id1) = sub_caminho[atual - 1]
                        (local2, enc_id2) = sub_caminho[atual]

                        cam = algoritmo(local1, local2)
                        logging.debug("Foi analisado o caminho: ")
                        logging.debug(caminho_to_string(cam))
                        caminhos_pos_algoritmos.append((cam, enc_id2))
                        total_este_caminho += calcula_distancia(cam)

                # Tem de voltar à base
                (local1, enc_id1) = sub_caminho[atual]
                cam = algoritmo(local1, origem_cidade)
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
        melhor_caminho_descoberto(estafeta_id, melhor_caminho)


# Gera todos os circuitos.
def gerar_circuitos(algoritmo):
    """
    Gera todos os circuitos baseando-se nas atribuições.
    @param algoritmo: Algoritmo usado para descobrir o caminho entre dois pontos.
    """
    lista_estafetas = {atribuicao.estafeta_id for atribuicao in atribuicoes}

    for estafeta in lista_estafetas:
        gera_entrega_um_estafeta(estafeta, algoritmo)
