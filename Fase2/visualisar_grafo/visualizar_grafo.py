import logging

from igraph import *

import algoritmos_procura.dfs
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import grafo1, local5, local10


def visualizar(grafo):
    g = converte_grafo(grafo)  # grafo do tipo igraph

    g.vs["label_dist"] = [-2 for v in g.vs]

    g.vs["label"] = g.vs["name"]
    g.es["width"] = g.es["weigth"]

    layout = g.layout("kk")

    plot(g, layout=layout)

    return g


def converte_grafo(grafo):
    g = Graph()

    for nodo in grafo.keys():
        g.add_vertex(nodo.nome)

    for nodo1, lista in grafo.items():
        for (nodo2, custo) in lista:
            g.add_edge(nodo1.nome, nodo2.nome, weigth=custo)
    return g


def ver_caminho(i_graph: Graph, caminho: [Local]):
    meter_cor(i_graph, caminho)
    # Atualiza a visualização do grafo
    plot(i_graph, layout=layout)


def meter_cor(i_graph: Graph, caminho: [Local]):
    lista = list()
    for i in range(len(i_graph.vs)):
        color = "black"
        if i_graph.vs["name"] in map(str, caminho):
            color = "red"
        lista.append(color)

    i_graph.vs["color"] = lista


def guardar_grafo(grafo, nome_ficheiro):
    plot(grafo, f"{nome_ficheiro}.png", )


def main():
    logging.basicConfig(level=logging.INFO)
    ver_caminho(converte_grafo(grafo1), algoritmos_procura.dfs.dfs(local5, local10))


main()
