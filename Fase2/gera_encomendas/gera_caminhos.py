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
from itertools import combinations, permutations

from base_conhecimento.baseConhecimento import encomendas


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

    # Fazer permutações
    permutacoes = list()
    for n in combinacoes:
        # Se receber [A, B], devolve [([A, B]), ([B, A]) ]
        # Logo, temos de adicionar cada uma das hipóteses, [A, B], e [B, A], às hipóteses
        temp = list(permutations(n))
        for x in temp:
            permutacoes.append(x)

    # Juntamos ao caminho atual as outras paragens, A e B fica [[A, B], [C]]
    # Aqui, recebemos após as permutações
    lista_final = []
    for uma_possibilidade in permutacoes:
        lista_final.append(adiciona_todas_paragens(uma_possibilidade, locais_entrega))

    # Adiciona o caso em que fazemos uma viagem por encomenda
    lista_final.append(paragens_individuais(locais_entrega))
    return lista_final
