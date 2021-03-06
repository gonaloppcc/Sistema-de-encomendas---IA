import logging
from math import sqrt
from random import randint

import networkx as nx
from matplotlib import pyplot as plt

from algoritmos_procura.common import calcula_norma
from algoritmos_procura.dfs import dfs
from base_conhecimento.baseConhecimento import mapa, origens, id_locais_cidades
from base_conhecimento.entidades.Local import Local

min_x = -10000
max_x = 10000

min_y = -10000
max_y = 10000

dist_min = 0.05 * sqrt((pow((max_x - min_x), 2) + pow((max_y - min_y), 2)))


def verifica_dist(nodo):
    """
    Verifica se o nodo que recebe como parâmetro se encontra a uma distância
    superior à definida em dist_min a todos os outros nodos do grafo a que pertence.
    @param nodo: Nodo a verificar
    @return True se o nodo estiver a pelo menos dist_min de todos os outros nodos
            False caso contrário
    """
    for outro_nodo in mapa["grafos"][nodo.freguesia]:
        if calcula_norma(nodo, outro_nodo) < dist_min:
            return False
    return True


def obtem_proximos(nodo):
    """
    Obtem a lista dos 5 nodos mais próximos ao nodo
    passado como argumento.
    @param nodo: Nodo a procurar
    @return: Lista com os 5 nodos mais próximos
    """
    lista = []
    for outro_nodo in mapa["grafos"][nodo.freguesia].keys():
        if nodo == outro_nodo:
            continue
        norma = calcula_norma(nodo, outro_nodo)
        lista.append((outro_nodo, norma))

    lista.sort(key=lambda x: x[1])
    return lista[0:5]


def gera_grafo(nome_grafo, num_nodos, probabilidade_conexao):
    g = nx.DiGraph()
    """
    Gera um grafo aleatório com num_nodos nodos e com o nome
    para nome_grafo. A origem é selecionada aleatoriamente
    e o algoritmo garante, através do uso do dfs, que a partir
    desta existe um caminho possível para todos os nodos.
    @param nome_grafo: Nome que o grafo terá no dicionário de grafos do mapa da base de conhecimento
    @param num_nodos: Número de nodos que o grafo irá ter
    @param probabilidade_conexao: Probabilidade de criar uma conexão entre cada dois nodos
    """
    mapa["grafos"][nome_grafo] = {}
    # Para inserir no id_locais_cidades da base de conhecimento.
    id_counter_antes = mapa['id_counter']
    # Gerar todos os nodos com nome 'Local_{i}' e freguesia 'Freguesia_{i}'.
    # As coordenadas são selecionadas aleatoriamente no campo de 0-100
    for i in range(num_nodos):
        freguesia = nome_grafo
        nome = f"Local_{mapa['id_counter'] + i}"
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
    # Acrescenta os ids incluídos nesta cidade.
    id_locais_cidades[nome_grafo] = (id_counter_antes, (mapa["id_counter"]))
    # Selecionar a origem aleatoriamente e adiciona-la ao
    # dicionário de origens em baseConhecimento
    origem = list(mapa["grafos"][nome_grafo])[randint(0, num_nodos - 1)]
    origens[nome_grafo] = origem
    logging.info(f"Origem: {origem.nome}")

    # Para cada nodo, percorrer todos os outros nodos
    # havendo uma probabilidade igual a probabilidade_conexao
    # de criar uma conexão entre eles.
    nodos = mapa["grafos"][nome_grafo].keys()
    for nodo in nodos:
        conectados = []
        lista = obtem_proximos(nodo)
        for outro_nodo, distancia in lista:
            if randint(0, 100) <= probabilidade_conexao:
                conectados.append((outro_nodo, distancia))
        mapa["grafos"][nome_grafo][nodo] = conectados

    # Percorrer todos os nodos para verificar que existe
    # um caminho possível entre estes e a origem selecionada anteriormente.
    # Aqui usamos o algoritmo depth-first porque não nos interessa que o
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

    for nodo, conexoes in mapa["grafos"][nome_grafo].items():
        g.add_node(nodo.id, pos=(nodo.x, nodo.y))
        logging.info(f"{nodo.nome}: ID: {nodo.id}, Freguesia: {nodo.freguesia}, x: {nodo.x}, y: {nodo.y}")
        for conectado, dist in conexoes:
            g.add_edge(nodo.id, conectado.id, distance=dist)
            logging.info(f"Ligação: {nodo.id} -> {conectado.id}")

    pos = nx.get_node_attributes(g, 'pos')
    nx.draw_networkx(g, pos, with_labels=True)
    plt.title(nome_grafo)
    plt.savefig(nome_grafo + ".png")
    plt.close()
