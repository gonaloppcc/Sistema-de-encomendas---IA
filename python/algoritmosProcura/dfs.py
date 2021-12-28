import baseConhecimento
from algoritmosProcura.common import conectados, print_caminho


def dfs2(origem, destino, listaAtual):
    # Caso chegue ao destino certo
    if origem == destino:
        return listaAtual
    # Caso seja um dead-end
    if origem not in baseConhecimento.distancias:
        return None
    ligados = conectados(origem)
    # Vamos guardar todos os caminhos não nulos
    # Por cada nó ligado ao atual
    for nodo in ligados:
        # Se o nó não tiver sido já visitado
        if nodo not in listaAtual:
            # Temos de guardar a lista porque, caso o dfs2 chegue a um dead-end
            # Temos de continuar a procurar, equivalente a backtrace
            listaAntesAlterar = listaAtual.copy()
            # Insere à cabeçaporque procuramos sempre o primeiro elemento da lista
            listaAtual.insert(0, nodo)

            # Chamada recursiva
            resRec = dfs2(nodo, destino, listaAtual)
            # Se der nulo, caminho não vai onde queremos, voltamos atrás
            # Caso contrário, retornamos o caminho válido
            if resRec is not None:
                return resRec
            else:  # Equivale ao backtrace
                listaAtual = listaAntesAlterar


def dfs(origem, destino):
    cam = dfs2(origem, destino, [origem])
    cam.reverse()
    return cam


# bfs
# Travessia de grafos, mas usei outro algoritmo
def bfs(origem, destino):
    # Guardamos os pares (nó atual, caminho até ele)
    queue = [(origem, [origem])]
    # Inicializamos todos os nodos como não visitados, num Map
    visitados = {}
    locais = baseConhecimento.distancias.keys()
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
                if visitados[node] == False:
                    visitados[node] = True
                    queue.append((node, path + [node]))


# Busca Iterativa Limitada em Profundidade.
# Eu fiz como diz no slide: T(5) Classical Search
# Este método Pesquisa em Profundidade Iterativa
def dfsLimited2(origem, destino, listaAtual, nivelAtual):
    if nivelAtual == 0:
        return None
        # Caso chegue ao destino certo
    if origem == destino:
        return listaAtual
    # Caso seja um dead-end
    if origem not in baseConhecimento.distancias:
        return None
    # Nós adjacentes ao atual (origem)
    ligados = conectados(origem)
    # Vamos guardar todos os caminhos não nulos
    # Por cada nó ligado ao atual
    for nodo in ligados:
        # Se o nó não tiver sido já visitado
        if nodo not in listaAtual:
            # Temos de guardar a lista porque, caso o dfs2 chegue a um dead-end
            # Temos de continuar a procurar, equivalente a backtrace
            listaAntesAlterar = listaAtual.copy()
            # Insere à cabeçaporque procuramos sempre o primeiro elemento da lista
            listaAtual.insert(0, nodo)

            # Chamada recursiva
            resRec = dfsLimited2(nodo, destino, listaAtual, nivelAtual - 1)
            # Se der nulo, caminho não vai onde queremos, voltamos atrás
            # Caso contrário, retornamos o caminho válido
            if resRec is not None:
                return resRec
            else:  # Equivale ao backtrace
                listaAtual = listaAntesAlterar
    return None


def dfsLimited(origem, destino):
    # Tenta procurar uma solução em cada nível
    lista = None
    nivelAtual = 1
    while lista == None:
        # Se a lista contiver algo, sai do ciclo
        lista = dfsLimited2(origem, destino, [origem], nivelAtual)
        nivelAtual += 1
    lista.reverse()
    return lista
