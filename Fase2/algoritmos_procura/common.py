# Funções para descobrir caminhos
# dfs, utilizando os diapositivos PL(8) das aulas
from math import sqrt

from base_conhecimento.baseConhecimento import mapa
from base_conhecimento.Local import Local


# Calcula a distância entre dois nodos através das suas coordenadas
def calcula_norma(nodo1, nodo2):
    return sqrt(pow((nodo2.x - nodo1.x), 2) + pow((nodo2.y - nodo1.y), 2))


def conectados(nodo):
    lista = []
    adjacentes = mapa["grafos"][nodo.freguesia].get(nodo)
    for (local, dist) in adjacentes:
        lista.append(local)
    return lista


def arestas(nodo):
    return mapa["grafos"][nodo.freguesia].get(nodo)


# Calcular distância
def calcula_distancia(nodos):
    if nodos is None:
        return None

    total = 0
    for i in range(len(nodos) - 1):
        nodos_connectados = mapa["grafos"][nodos[i].freguesia][nodos[i]]
        for nome, dist in nodos_connectados:
            if nome.nome == nodos[i + 1].nome:
                total += dist
    return total


# Calcular tempos e velocidades a partir de entregas
def calcula_tempo_transporte(meio_transporte, peso_encomenda, distancia):
    velocidade_transporte = meio_transporte.calcula_velocidade(peso_encomenda)
    if velocidade_transporte == 0:
        raise Exception("O meio de transporte não consegue levar a encomenda")
    return distancia / velocidade_transporte


def caminho_to_string(cam: [Local]):
    caminho = "Caminho: "
    for nodo in cam:
        caminho = caminho + f"{nodo.nome} "

    return caminho
