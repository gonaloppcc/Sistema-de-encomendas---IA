from base_conhecimento.baseConhecimento import mapa
from base_conhecimento.Local import Local
from algoritmos_procura.common import conectados


def dfs2(origem, destino, lista_atual):
    # Caso chegue ao destino certo
    if origem == destino:
        return lista_atual
    # Caso seja um dead-end
    if origem not in mapa["grafos"][origem.freguesia]:
        return None
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
            res_rec = dfs2(nodo, destino, lista_atual)
            # Se der nulo, caminho não vai onde queremos, voltamos.
            # Caso contrário, retornamos o caminho válido
            if res_rec is not None:
                return res_rec
            else:  # Equivale ao backtrace
                lista_atual = lista_antes_alterar


def dfs(origem: Local, destino: Local):
    cam = dfs2(origem, destino, [origem])
    if cam is not None:
        cam.reverse()
    return cam
