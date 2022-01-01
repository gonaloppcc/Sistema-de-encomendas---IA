from functools import reduce
from itertools import combinations
from math import inf

from gera_encomendas.Entrega import Entrega
from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte, maximo_peso_uma_viagem, print_caminho
from algoritmos_procura.dfs import dfs
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, locais, origens, transportes

# TODO: Passar isto para metodos de instancia da classe Entrega?

# Variáveis globais

# Entregas realizadas
entregas_feitas = []

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico ← Falta implementar
flag_ecologico_ou_rapido = False


# Escolhe o veículo que pode entregar uma encomenda.
# Recebe o caminho e a encomenda, e a partir do peso vê qual o melhor veículo para a entregar.
# Para já, só vê em função da velocidade, falta ver um critério para o ser "verde".
def escolhe_veiculo(cam, peso_encomenda):
    distancia_caminho = calcula_distancia(cam)
    if not flag_ecologico_ou_rapido:
        tempo_transporte = 100000000
        melhor_veiculo = transportes[0]

        for veiculo in transportes:
            try:
                tempo_veiculo = calcula_tempo_transporte(veiculo, peso_encomenda, distancia_caminho)
                # print("Passa pelo veiculo: ", veiculo.nome)
                # print("Com tempo de entrega: ", tempo_veiculo)
                if tempo_veiculo < tempo_transporte:
                    tempo_transporte = tempo_veiculo
                    melhor_veiculo = veiculo
            except:
                pass
        return melhor_veiculo


# Gera uma entrega a partir da atribuição
def gerar_entrega(estafeta, encomenda):
    cidade_estafeta = estafeta.cidade
    cidade_encomenda = locais.get(encomenda.id_local_entrega).freguesia
    if cidade_estafeta is not cidade_encomenda:
        print("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = locais.get(encomenda.id_local_entrega)

    # Para mudar o algoritmo é aqui

    # cam = dfs(origens.get(cidade_estafeta), local_entrega)
   # veiculo = escolhe_veiculo(cam, encomenda)
   # entrega_feita = Entrega(encomenda.encomenda_id, estafeta.estafeta_id, 0, veiculo, cam)
   # return entrega_feita


# Descobre todas as encomendas que um dado estafeta deve fazer
def entregas_do_estafeta(estafeta):
    list_encomendas = []
    for atribuicao1 in atribuicoes:
        if atribuicao1.estafeta_id == estafeta:
            list_encomendas.append(atribuicao1.encomenda_id)
    return list_encomendas


"""
Esta função recebe qual é o estefeta que vamos analisar, e devolve uma lista de listas com as possíveis entregas que ele pode fazer.
Por exemplo, se o estafeta 1 tiver que entregas a encomenda A, B e C, ele vai devolver a seguinte lista:
[
([A], [B], [C]), 
[[A, B], [C]),
[[A], [B, C]],
[[A, B, C]],
]
Como cada estefeta só entrega na sua cidade, vamos procurar todos os possíveis percursos, independentemente do custo.
"""


# Função simples para ver se uma paragem pertence a uma lista ou sublista
def pertence(elem, lista_de_listas):
    for lista in lista_de_listas:
        if elem in lista:
            return True
    return False


# A um conjunto de paragens, adiciona as outras todas juntas.
# Por exemplo, se tivermos as paragens A, B e C, e recebermos a lista [A, B], ele retorna:
# [A , B], [C]
def adiciona_todas_paragens(uma_possibilidade, locais_entrega):
    lista_atual = [list(uma_possibilidade)]
    for uma_paragem in locais_entrega:
        if not pertence(uma_paragem, lista_atual):
            lista_atual.append([uma_paragem])
    return lista_atual


# Adiciona as paragens individualmente. Não usamos o subset para não ter paragens repetidas
# [A, B, C] -> [[A], [B], [C]]
def paragens_individuais(locais_entrega):
    lista_individuais = []
    for um_local in locais_entrega:
        lista_individuais.append([um_local])
    return lista_individuais


# Esta função gera todos os caminhos possíveis para entregar uma encomenda.
# Por exemplo, se tiver de passar por três locais, pode entregar uma encomenda por viagem, duas ou até três.
# Para isso, ela procura todos os locais de entrega que um estafeta tem de passar, a partir dos ids das encomendas.
# Depois faz combinações desses locais. Por exemplo: [A, B, C] fica A | B | C | A, B | A, C | B, C | A, B, C
# Mas excluímos os casos da lista separada, que são acrescentados no fim
# A seguir, guardamos em listas os percursos, usando o exemplo de à bocado: se passa em A e B, tem de haver uma viagem só para C
def descobre_possiveis_caminhos(encomendasID):
    # Guardamos em set para não termos locais repetidos
    locais_entrega = set(map(lambda encomendaID: encomendas.get(encomendaID).id_local_entrega, encomendasID))
    # Já temos todos os locais de entrega

    # Obter todos os subcaminhos, com 2 paragens
    combinacoes = list()
    for n in range(2, len(locais_entrega) + 1):
        combinacoes += list(combinations(locais_entrega, n))

    # Juntamos ao caminho atual as outras paragens, A e B fica [[A, B], [C]]
    lista_final = []
    for uma_possibilidade in combinacoes:
        lista_final.append(adiciona_todas_paragens(uma_possibilidade, locais_entrega))

    # Adiciona o caso em que fazemos uma viagem por encomenda
    lista_final.append(paragens_individuais(locais_entrega))

    for um in lista_final:
        print("[Descobre possiveis caminhos] Uma hipótese de caminho é: ", um)
    return lista_final

#Descobre os ids das encomendas que são entregues num dado percurso.
#Necessário para ver se é possível entregar todas as encomendas associadas a esse nodo
#E na parte final de gerar as entregas
def encomendas_nesse_percurso(percurso, encomendas_id):
    encomendas_id_local = []
    for id in encomendas_id:
        if encomendas.get(id).id_local_entrega in percurso:
            encomendas_id_local.append(id)
    return encomendas_id_local

#Verifica se é possível fazer o percurso associado a uma lista de destinos
# Um caminho possível é do tipo: [[A, B, C], [D]]
def possivel_por_pesos(um_caminho_possivel, encomendas_id):
    maximo_possivel = maximo_peso_uma_viagem()
    #Um exemplo dum subcaminho: [A, B, C]
    for sub_caminho in um_caminho_possivel:
        #Ids das encomendas entregues neste percurso
        encomendas_no_percurso = encomendas_nesse_percurso(sub_caminho, encomendas_id)
        #Vai buscar o peso de cada encomenda
        pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, encomendas_no_percurso)
        peso_no_sub_caminho = sum(pesos_no_percurso)
        if peso_no_sub_caminho > maximo_possivel:
            print("[geraEntregas] Um caminho foi descartado: ", peso_no_sub_caminho, " > ", maximo_possivel)
            return False
    return True

# Gera as entregas de um dado estafeta. Recebe o algoritmo usado para o cálculo dos caminhos
def gera_entrega_um_estafeta(estafeta_id, algoritmo):
    estafeta = estafetas.get(estafeta_id)
    print("Vamos analisar o estafeta nr.: ", estafeta_id)
    # Encomendas que o estafeta vai entregar
    encomendas_id = entregas_do_estafeta(estafeta_id)
    # Combinações dos possíveis caminhos que o estafeta pode usar
    possiveis_percursos = descobre_possiveis_caminhos(encomendas_id)
    # Local do centro de entregas, ele tem de partir e voltar para lá
    origem_cidade = origens.get(estafeta.cidade)

    # Guardam as melhores distâncias e caminhos
    melhor_distancia = float(inf)
    #Guarda os caminhos do melhor
    melhor_caminho = []
    #um caminho possível = [[A, B, C], [D]]
    for um_caminho_possivel in possiveis_percursos:
        #Verificamos se é possível fazer este percurso com as paragens atuais
        if possivel_por_pesos(um_caminho_possivel, encomendas_id):

            total_este_caminho = 0
            caminhos_pos_algoritmos = []
            print("[gera entrega um estafeta1] Um caminho possível é: ", um_caminho_possivel)
            for sub_caminho in um_caminho_possivel:
                # Verifica o total de distância deste caminho
                # [A, B, C]
                print("[gera entrega um estafeta1] Um sub caminho é: ")
                for x in sub_caminho: print("um: ", x.nome)
                for atual in range(0, len(sub_caminho)):
                    # Se for a primeira paragem, tem de sair da base
                    if atual == 0:
                        cam = algoritmo(origem_cidade, sub_caminho[atual])
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append(cam)
                        total_este_caminho += calcula_distancia(cam)
                    else:
                        cam = algoritmo(sub_caminho[atual - 1], sub_caminho[atual])
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append(cam)

                        total_este_caminho += calcula_distancia(cam)
                # Tem de voltar à base
                print("[gera entrega um estafeta3] O caminho que está a procurar é: ", sub_caminho[atual].nome, " para ", origem_cidade.nome)
                cam = algoritmo(sub_caminho[atual], origem_cidade)
                print("Foi analisado o caminho: ")
                print_caminho(cam)
                total_este_caminho += calcula_distancia(cam)
                caminhos_pos_algoritmos.append(cam)

            if total_este_caminho < melhor_distancia:
                print("Altera caminho para um melhor, ", total_este_caminho)
                melhor_distancia = total_este_caminho
                melhor_caminho.clear()
                melhor_caminho = caminhos_pos_algoritmos.copy()
    #nenhum caminho é possível, pode ser porque a encomenda é muito pesada
    #Ou duas, ou mais, entregas dum nodo ultrapassa o máximo.
    if melhor_distancia == float(inf):
        print("Nenhuma foi entregue")
    else:
        maximo_possivel = maximo_peso_uma_viagem()
        print("[gera entregas] <---------Tudo gerado-------->")

        for sub_percurso_atual in range(0, len(melhor_caminho)-1):
            print("<--Entrega-->")
            #Primeiro, vamos ver que encomendas serão entregues nessa viagem
            ids = encomendas_nesse_percurso(melhor_caminho[sub_percurso_atual], encomendas_id)
            pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, ids)
            peso_no_sub_caminho = sum(pesos_no_percurso)
            veiculo = escolhe_veiculo(melhor_caminho[sub_percurso_atual], peso_no_sub_caminho)
            entrega_feita = Entrega(ids, estafeta_id, 0, veiculo, melhor_caminho[sub_percurso_atual])
            entrega_feita.imprime_entrega()

        print("E o caminho de voltar")
        print_caminho(melhor_caminho[len(melhor_caminho)-1])



# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas(algoritmo):
    lista_estafetas = {atribuicao.estafeta_id for atribuicao in atribuicoes}

    for estafeta in lista_estafetas:
        gera_entrega_um_estafeta(estafeta, algoritmo)

        print("<------------------>")


""" Versão ANTIGA
    for atribuicao in atribuicoes:
        entrega = gerar_entrega(atribuicao)
        if entrega is not None:
            entregas_feitas.append(entrega)
            entrega.imprime_entrega()
            print("<------------------>")
            """
