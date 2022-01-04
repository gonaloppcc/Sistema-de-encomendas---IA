# Funções para descobrir caminhos
# dfs, utilizando os diapositivos PL(8) das aulas

from base_conhecimento import baseConhecimento
from base_conhecimento.baseConhecimento import transportes
from base_conhecimento import baseConhecimento, Local

from math import sqrt




# Calcula a distância entre dois nodos através das suas coordenadas
def calcula_norma(nodo1, nodo2):
    return sqrt(pow((nodo2.x - nodo1.x), 2) + pow((nodo2.y - nodo1.y), 2))


def conectados(nodo):
    lista = []
    adjacentes = baseConhecimento.grafo1.get(nodo)
    for (local, dist) in adjacentes:
        lista.append(local)
    return lista


def arestas(nodo):
    return baseConhecimento.grafo1.get(nodo)


# Calcular distância
def calcula_distancia(nodos):
    if nodos is None:
        return None

    total = 0
    for i in range(len(nodos) - 1):
        nodos_connectados = baseConhecimento.grafo1[nodos[i]]
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




# Calcual o máximo de peso que podemos levar numa dada viagem, a partir do máximo que os veículos podem transportar
def maximo_peso_uma_viagem():
    """
    Descobre qual o peso máximo que conseguimos transportar num circuito.
    @return: Peso máximo, em Kgs.
    """
    max = 0
    for veiculo in transportes:
        if veiculo.peso_maximo >= max:
            max = veiculo.peso_maximo
    return max

def caminho_to_string(cam: [Local]):
    caminho = "Caminho: "
    for nodo in cam:
        caminho = caminho + f"{nodo.nome} "

    return caminho

