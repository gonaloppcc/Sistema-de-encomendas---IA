from algoritmos_procura.common import conectados, calcula_norma
from base_conhecimento.baseConhecimento import mapa


# Função auxiliar que retorna o
# elemento de ordenação para o sort
# da lista de nodos ligados.
# Neste caso é a estima.
def get_norma(p):
    return p[1]


def gulosa(origem, destino, lista_atual):
    if origem == destino:
        return lista_atual
    if origem not in mapa["grafos"][origem.freguesia]:
        return None
    ligados = conectados(origem)
    # Calculamos a estima e ordenamos os nodos com base nesta
    ligados_sorted = []
    for nodo in ligados:

        norma = calcula_norma(nodo, destino)
        ligados_sorted.append((nodo, norma))
    ligados_sorted.sort(key=get_norma)
    # Procurar o caminho a começar pelos nodos
    # com melhor estima
    for (nodo, norma) in ligados_sorted:
        if nodo not in lista_atual:
            lista_antes_alterar = lista_atual.copy()
            lista_atual.insert(0, nodo)
            resultado = gulosa(nodo, destino, lista_atual)
            if resultado is not None:
                return resultado
            else:
                lista_atual = lista_antes_alterar


def resolve_gulosa(origem, destino):
    cam = gulosa(origem, destino, [origem])
    if cam is not None:
        cam.reverse()
    return cam
