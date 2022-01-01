import networkx as nx

from base_conhecimento.baseConhecimento import grafo1

grafo = nx.MultiGraph(grafo1)

g = nx.Graph()

g.add_node("node1")
g.add_node("node2")

g.add_edge("node1", "node2")
g.add_edge("node2", "node3")
g.add_edge("node3", "node4")
g.add_edge("node4", "node1")

# nx.draw(g, with_labels=True)

for node in grafo.nodes:
    print(f"Nodos conectados ao nodo {node}: {grafo.neighbors(node)}")
    for neighbor in grafo.neighbors(node):
        print(neighbor[0])

print(dict(nx.all_neighbors(g, 'node1'))[0])

# plt.show()
