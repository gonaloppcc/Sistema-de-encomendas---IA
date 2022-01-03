from random import randint
import networkx as nx
import matplotlib.pyplot as plt

from algoritmos_procura.common import calcula_norma
from algoritmos_procura.dfs import dfs
from base_conhecimento import baseConhecimento
from base_conhecimento.Local import Local


def gera_grafo(nome_grafo, num_nodos):
    """
    Gera um grafo aleatório com num_nodos nodos e com o nome
    para nome_grafo. A origem é selecionada aleatóriamente
    e o algoritmo garante, através do uso do dfs, que a partir
    desta existe um caminho possível para todos os nodos.
    :param nome_grafo: Nome que o grafo terá no dicionário origens em baseConhecimento
    :param num_nodos: Número de nodos que o grafo ter
    """
    g = nx.DiGraph()
    # Gerar todos os nodos com nome 'Local_{i}' e freguesia 'Freguesia_{i}'.
    # As coordenadas são selecionadas aleatóriamente no campo de 0-100.
    for i in range(num_nodos):
        freguesia = f"Freguesia_{i}"
        nome = f"Local_{i}"
        x = randint(0, 100)
        y = randint(0, 100)
        local = Local(i, freguesia, nome, x, y)
        baseConhecimento.locais[i] = local,
        g.add_node(nome, pos=(x, y))
        print(f"Coordenadas{nome}: x={x}, y={y}")

    # Selecionar a origem aleatóriamente e adicioná-la ao
    # dicionário de origens
    origem = baseConhecimento.locais[randint(0, num_nodos-1)]
    baseConhecimento.origens[nome_grafo] = origem

    # Para cada nodo percorrer todos os outros nodos
    # havendo uma probabilidade de 50% de criar uma conexão
    # entre eles.
    nodos = baseConhecimento.locais.values()
    for nodo in nodos:
        conectados = []
        for outro_nodo in nodos:
            if nodo == outro_nodo:
                continue
            if randint(0, 1):
                distancia = calcula_norma(nodo[0], outro_nodo[0])
                conectados.append((outro_nodo, distancia))
                g.add_edge(nodo[0].nome, outro_nodo[0].nome)
        baseConhecimento.grafo1[nodo] = conectados

    # Percorrer todos os nodos para veríficar que existe
    # um caminho possível entre estes e a origem selecionada anteriormente.
    # Aqui usamos o alguritmo depth-first porque não nos interessa que o
    # caminho encontrado seja o mais rápido. Interessa-nos só que exista
    # um caminho.
    for nodo in nodos:
        if not dfs(origem, nodo) is not None:
            distancia = calcula_norma(origem[0], nodo[0])
            baseConhecimento.grafo1[origem].append((nodo[0], distancia))
            g.add_edge(origem[0].nome, nodo[0].nome)

    print(origem[0].nome)

    fig, ax = plt.subplots()
    pos = nx.get_node_attributes(g, 'pos')
    nx.draw_networkx(g, pos, ax=ax)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.title("Foda-se")
    plt.show()


gera_grafo("grafo_teste", 5)
