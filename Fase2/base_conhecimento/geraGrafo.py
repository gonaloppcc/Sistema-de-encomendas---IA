from math import sqrt
from random import randint

from algoritmos_procura.common import calcula_norma
from algoritmos_procura.dfs import dfs
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import mapa, origens

min_x = -10000
max_x = 10000

min_y = -10000
max_y = 10000

dist_min = 0.05 * sqrt((pow((max_x - min_x), 2) + pow((max_y - min_y), 2)))


def verifica_dist(nodo):
    for outro_nodo in mapa["grafos"][nodo.freguesia]:
        if calcula_norma(nodo, outro_nodo) < dist_min:
            return False
    return True


def gera_grafo(nome_grafo, num_nodos, probabilidade_conexao):
    """
    Gera um grafo aleatório com num_nodos nodos e com o nome
    para nome_grafo. A origem é selecionada aleatóriamente
    e o algoritmo garante, através do uso do dfs, que a partir
    desta existe um caminho possível para todos os nodos.
    :param nome_grafo: Nome que o grafo terá no dicionário origens em baseConhecimento
    :param num_nodos: Número de nodos que o grafo ter
    :param probabilidade_conexao: Probabilidade de criar uma conexão de cada nodo
    """
    mapa["grafos"][nome_grafo] = {}
    # Gerar todos os nodos com nome 'Local_{i}' e freguesia 'Freguesia_{i}'.
    # As coordenadas são selecionadas aleatóriamente no campo de 0-100
    for i in range(num_nodos):
        freguesia = nome_grafo
        nome = f"Local_{i}"
        out = False
        local = None
        while not out:
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            local = Local(mapa["id_counter"] + i, freguesia, nome, x, y)
            out = verifica_dist(local)
        mapa["grafos"][nome_grafo][local] = []

    # Incrementar o id_counter para o novo max_id
    mapa["id_counter"] += num_nodos
    # Selecionar a origem aleatóriamente e adicioná-la ao
    # dicionário de origens
    origem = list(mapa["grafos"][nome_grafo])[randint(0, num_nodos - 1)]
    origens[nome_grafo] = origem

    # Para cada nodo percorrer todos os outros nodos
    # havendo uma probabilidade de 50% de criar uma conexão
    # entre eles.
    nodos = mapa["grafos"][nome_grafo].keys()
    for nodo in nodos:
        conectados = []
        for outro_nodo in nodos:
            if nodo == outro_nodo:
                continue
            if randint(0, 100) <= probabilidade_conexao:
                distancia = calcula_norma(nodo, outro_nodo)
                conectados.append((outro_nodo, distancia))
        mapa["grafos"][nome_grafo][nodo] = conectados

    # Percorrer todos os nodos para veríficar que existe
    # um caminho possível entre estes e a origem selecionada anteriormente.
    # Aqui usamos o alguritmo depth-first porque não nos interessa que o
    # caminho encontrado seja o mais rápido. Interessa-nos só que exista
    # um caminho.
    # Caso o caminho não exista, criamos uma ligação direta entre estes.
    for nodo in nodos:
        if dfs(origem, nodo) is None:
            distancia = calcula_norma(origem, nodo)
            mapa["grafos"][nome_grafo][origem].append((nodo, distancia))

    # O mesmo que no passo anterior mas para verificar que o estafeta,
    # depois de uma entrega, tem um caminho de volta para o armazém.
    for nodo in nodos:
        if dfs(nodo, origem) is None:
            distancia = calcula_norma(nodo, origem)
            mapa["grafos"][nome_grafo][nodo].append((origem, distancia))
