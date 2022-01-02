import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
i = 1
G.add_node(i, pos=(i, i))
G.add_node(2, pos=(2, 2))
G.add_node(3, pos=(1, 0))
G.add_edge(1, 2, weight=0.5)
G.add_edge(1, 3, weight=9.8)
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

"""import networkx as nx
from matplotlib import pyplot as plt

from base_conhecimento.baseConhecimento import grafo1

grafo = nx.MultiGraph(grafo1)

g = nx.DiGraph()

g.add_node("node1")
g.add_node("node2")

g.add_edge("node1", "node2", weight=5)
g.add_edge("node2", "node3", weight=6)
g.add_edge("node3", "node4", weight=8)
g.add_edge("node4", "node1", weight=3)

#nx.draw(g, with_labels=True)
labels = nx.get_edge_attributes(g,'weight')
pos=nx.get_node_attributes(g,'pos')

nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

"""
for node in grafo.nodes:
    print(f"Nodos conectados ao nodo {node}: {grafo.neighbors(node)}")
    for neighbor in grafo.neighbors(node):
        print(neighbor[0])
"""
#print(dict(nx.all_neighbors(g, 'node1'))[0])

plt.show()
"""
