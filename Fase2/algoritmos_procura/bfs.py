from algoritmos_procura.common import conectados

# bfs
# Travessia de grafos, mas usei outro algoritmo
from base_conhecimento.baseConhecimento import mapa


def bfs(origem, destino):
    # Guardamos os pares (nó atual, caminho até ele)
    queue = [(origem, [origem])]
    # Inicializamos todos os nodos como não visitados, num Map
    visitados = {}
    #    locais = baseConhecimento.distancias.keys()
    cidade = origem.encontra_cidade()
    locais = mapa["grafos"][cidade].keys()
    for umaKey in locais:
        visitados[umaKey] = False

    while queue:
        vertex, path = queue.pop(0)
        visitados[vertex] = True
        # Por cada nó adjacente ao atual, temos de o verificar
        for node in conectados(vertex):
            # Se o nó for o destino, devolvemos o caminho até ao "node" mais o próprio node
            if node == destino:
                return path + [destino]
            else:
                # Se o nó não foi visitado, adicionamos o nó atual à queue, com o caminho até ele
                if not visitados[node]:
                    visitados[node] = True
                    queue.append((node, path + [node]))
