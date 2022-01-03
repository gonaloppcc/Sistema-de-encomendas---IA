from random import randint
import networkx as nx
import matplotlib.pyplot as plt

from base_conhecimento import baseConhecimento
from base_conhecimento.Local import Local


def gera_grafo(num_nodos):
    g = nx.DiGraph()
    for i in range(num_nodos):
        freguesia = f"Freguesia_{i}"
        nome = f"Local_{i}"
        x = randint(0, 100)
        y = randint(0, 100)
        local = Local(i, freguesia, nome, x, y)
        baseConhecimento.locais[i] = local,
        g.add_node(nome)
    test = baseConhecimento.locais.values()

    for nodo in test:
        conectados = []
        for outro_nodo in test:
            if nodo == outro_nodo:
                continue
            conecta = randint(0, 1)
            if conecta:
                distancia = randint(0, 50)
                conectados.append((outro_nodo, distancia))
                g.add_edge(nodo[0].nome, outro_nodo[0].nome)
        baseConhecimento.grafo1[nodo] = conectados
    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    plt.title("Foda-se")
    plt.show()
