from math import inf

from algoritmos_procura.common import calcula_distancia, maximo_peso_uma_viagem, print_caminho
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, origens
from base_conhecimento.circuitos import adiciona_circuito
# Entregas realizadas
from gera_encomendas.gera_caminhos import descobre_possiveis_caminhos


# TODO: Passar isto para metodos de instancia da classe Entrega?


def entregas_do_estafeta(estafeta):
    """
    Descobre todas as encomendas que um dado estafeta deve fazer, pelas atribuições da base de conhecimento.
    @param estafeta: Id do estafeta
    @return: Id's das encomendas que o estafeta deve entregar.
    """
    list_encomendas = []
    for atribuicao1 in atribuicoes:
        if atribuicao1.estafeta_id == estafeta:
            list_encomendas.append(atribuicao1.encomenda_id)
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
            print("Este percurso não consegue entregar as encomendas")
            return False
        print(" ")
    return True


def gera_entrega_um_estafeta(estafeta_id, algoritmo):
    """
    Gera as entregas de um dado estafeta. Recebe o algoritmo usado para o cálculo dos caminhos.
    @param estafeta_id: Estefeta que queremos analisar.
    @param algoritmo: Qual o algoritmo a usar para gerar os percursos entre paragens.
    """
    estafeta = estafetas.get(estafeta_id)
    print("Vamos analisar o estafeta nr.: ", estafeta_id)
    # Encomendas que o estafeta vai entregar.
    encomendas_id = entregas_do_estafeta(estafeta_id)
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
                print("[gera entrega um estafeta1] Um sub caminho é: ")
                for (local, _) in sub_caminho: print("um: ", local.nome)
                for atual in range(0, len(sub_caminho)):
                    # Se for a primeira paragem, tem de sair da base
                    if atual == 0:
                        (local, enc_id) = sub_caminho[atual]
                        cam = algoritmo(origem_cidade, local)
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append((cam, enc_id))
                        total_este_caminho += calcula_distancia(cam)
                    else:
                        # Liga as outras duas paragens
                        (local1, enc_id1) = sub_caminho[atual - 1]
                        (local2, enc_id2) = sub_caminho[atual]

                        cam = algoritmo(local1, local2)
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append((cam, enc_id2))
                        total_este_caminho += calcula_distancia(cam)

                # Tem de voltar à base
                (local1, enc_id1) = sub_caminho[atual]
                cam = algoritmo(local1, origem_cidade)
                print("Foi analisado o caminho: ")
                print_caminho(cam)
                total_este_caminho += calcula_distancia(cam)
                print("Este caminho tem o custo total de: ", total_este_caminho)
                caminhos_pos_algoritmos.append((cam, -1))
            print("<---------Fim de análise de um caminho------->")
            if total_este_caminho < melhor_distancia:
                print("Altera caminho para um melhor, ", total_este_caminho)
                # Guarda as informações do melhor caminho
                melhor_distancia = total_este_caminho
                melhor_caminho.clear()
                melhor_caminho = caminhos_pos_algoritmos.copy()
    # Nenhum caminho é possível, pode ser porque a encomenda é muito pesada
    # Ou duas, ou mais, entregas dum nodo ultrapassa o máximo.
    if melhor_distancia == float(inf):
        print("Nenhuma foi entregue")
    else:
        maximo_possivel = maximo_peso_uma_viagem()
        print("[gera entregas] <---------Tudo gerado-------->")
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
                print("Gera circuito")
                for uma_encomenda in encomendas_entregues_neste_circuito: print("Encomenda id: ", uma_encomenda)
                print("Caminho: ")
                print_caminho(circuito_atual)
                adiciona_circuito(circuito_atual, encomendas_entregues_neste_circuito, estafeta_id)
                circuito_atual.clear()
                encomendas_entregues_neste_circuito.clear()
            else:
                encomendas_entregues_neste_circuito.append(enc_id)


# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas(algoritmo):
    lista_estafetas = {atribuicao.estafeta_id for atribuicao in atribuicoes}

    for estafeta in lista_estafetas:
        gera_entrega_um_estafeta(estafeta, algoritmo)

