from Fase2.algoritmos_procura.common import conectados
from Fase2.base_conhecimento import baseConhecimento


# Busca Iterativa Limitada em Profundidade.
# Eu fiz como diz no ‘diapositivo’: T(5) Classical Search
# Este método Pesquisa em Profundidade Iterativa
def dfs_limited2(origem, destino, lista_atual, nivel_atual):
    if nivel_atual == 0:
        return None
        # Caso chegue ao destino certo
    if origem == destino:
        return lista_atual
    # Caso seja um dead-end
    if origem not in baseConhecimento.distancias:
        return None
    # Nós adjacentes ao atual (origem)
    ligados = conectados(origem)
    # Vamos guardar todos os caminhos não nulos
    # Por cada nó ligado ao atual
    for nodo in ligados:
        # Se o nó não tiver sido já visitado
        if nodo not in lista_atual:
            # Temos de guardar a lista porque, caso o dfs2 chegue a um dead-end
            # Temos de continuar a procurar, equivalente a backtrace
            lista_antes_alterar = lista_atual.copy()
            # Insere à cabeçaporque procuramos sempre o primeiro elemento da lista
            lista_atual.insert(0, nodo)

            # Chamada recursiva
            res_rec = dfs_limited2(nodo, destino, lista_atual, nivel_atual - 1)
            # Se der nulo, caminho não vai onde queremos, voltamos.
            # Caso contrário, retornamos o caminho válido
            if res_rec is not None:
                return res_rec
            else:  # Equivale ao backtrace
                lista_atual = lista_antes_alterar
    return None


def dfs_limited(origem, destino):
    # Tenta procurar uma solução em cada nível
    lista = None
    nivel_atual = 1
    while lista is None:
        # Se a lista contiver algo, sai do ciclo
        lista = dfs_limited2(origem, destino, [origem], nivel_atual)
        nivel_atual += 1
    lista.reverse()
    return lista
