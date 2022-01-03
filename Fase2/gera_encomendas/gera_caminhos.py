"""
Este ficheiro gera os vários percursos que podem ser realizados por um estafeta para entregar todas as encomendas que tem atribuídas.
Por isso, devolvemos uma lista com conjuntos de percursos. Esse conjunto de percursos tem de incluir todas as encomendas.
Aqui, um percursos é um conjunto de paragens, associadas ao ID da encomenda que será entregue.

Ignorando os id's das entregas, teremos algo deste género para as paragens A, B e C:
[
([A], [B], [C]),  <- três percursos, com cada um a entregar uma encomenda.
[[A, B], [C]),    <- dois percursos, um entrega duas encomendas, outro entrega só uma.
[[B, A], [C]),    <- Igual ao anterior, mas troca a ordem.
[[A], [B, C]],    <- dois percursos, um entrega duas encomendas, outro entrega só uma.
[[A], [C, B]],    <- Igual ao anterior, mas troca a ordem
[[A, B, C]],      <- um percursos, A entregar todas as encomendas.
[[A, C, B]]       <- Um exemplo de uma permutação. Acrescentamos todas as hipóteses possíveis de entregar.
]
Como cada estefeta só entrega na sua cidade, vamos procurar todos os possíveis percursos, independentemente do custo.
"""

# Função simples para ver se uma paragem pertence a uma lista ou sublista
from itertools import combinations, permutations

from base_conhecimento.baseConhecimento import encomendas


def pertence(elem, lista_de_listas) -> bool:
    """
    Função que verifica se um elemento pertence a uma conjunto de listas. 
    @return: Se o elemento pertence ou não.
    """
    for lista in lista_de_listas:
        if elem in lista:
            return True
    return False


#
def adiciona_todas_paragens(circuitos_incompletos, todas_as_paragens):
    """
    A um conjunto de circuitos incompletos, adiciona as restantes encomendas que é necessário entregar.
    Por exemplo, se tivermos as paragens A, B e C, e recebermos a lista [A, B], ele retorna:
    [A , B], [C]. As paragens A e B são feitas ao mesmo tempo, e a C é feita numa viagem à parte.
    @param circuitos_incompletos: Percursos avaliados até agora.
    @param todas_as_paragens: Todas as paragens
    @return: Circuito completo que passa por todos os locais de entregas das encomendas.
    """
    lista_atual = [list(circuitos_incompletos)]
    for uma_paragem in todas_as_paragens:
        # Se uma paragem não pertence ao circuito atual, adiciona-se.
        if not pertence(uma_paragem, lista_atual):
            lista_atual.append([uma_paragem])
    return lista_atual


def paragens_individuais(locais_entrega):
    """
    Adiciona as paragens individualmente. Por exemplo, se tivermos de passar pelos locais A, B e C, geramos a seguinte lista:
    [A, B, C] -> [[A], [B], [C]]
    @param locais_entrega: Locais por onde temos de passar.
    @return: Percursos compostos por apenas uma paragem.
    """
    lista_individuais = []
    for um_local in locais_entrega:
        lista_individuais.append([um_local])
    return lista_individuais


#
def descobre_possiveis_caminhos(encomendasID):
    """
    Esta função gera todos os caminhos possíveis para entregar uma encomenda.
    Por exemplo, se tiver de passar por três locais, pode entregar uma encomenda por viagem, duas ou até três.
    Para isso, ela procura todos os locais de entrega que um estafeta tem de passar, a partir dos ids das encomendas.
    Depois faz combinações desses locais. Por exemplo: [A, B, C] fica A | B | C | A, B | A, C | B, C | A, B, C
    Mas excluímos os casos da lista separada, que são acrescentados no fim
    A seguir, guardamos em listas os percursos, usando o exemplo de à bocado: se passa em A e B, tem de haver uma viagem só para C
    @param encomendasID: Encomendas para as quais temos de gerar os percursos possíveis.
    @return: As possibilidades de percurso.
    """
    # Guardamos em set para não termos locais repetidos
    locais_entrega = set(
        map(lambda encomendaID: (encomendas.get(encomendaID).id_local_entrega, encomendaID), encomendasID))
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
    print("[gera_caminhos] Lista final da gera_caminhos")
    # Uma possibilidade é um conjunto de caminhos.
    # Essa possibilidade entrega todas as encomendas previstas.
    # É do tipo:
    # [ [ (local1, Encomenda1),(local2, Encomenda2)] ] (tudo num caminho) ou
    # [ [(local1, Encomenda1)],[(local2, Encomenda2)] ] (dois caminhos)
    for possibilidade in lista_final:
        # Temos um percurso inteiro. Por exemplo:
        # [(local1, Encomenda1), (local2, Encomenda2)]
        for caminho in possibilidade:
            print("[gera_caminhos] Um caminho: ")
            # Cada paragem do percurso
            for (local, encID) in caminho:
                print(" ", local.nome, " | ", encID, end='')
            print(" ")
        print(" ")

    return lista_final
