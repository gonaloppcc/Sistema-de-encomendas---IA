# Funções para descobrir caminhos
# dfs, utilizando os diapositivos PL(8) das aulas
from base_conhecimento import baseConhecimento, Local
from math import sqrt


# Calcula a distância entre dois nodos através das suas coordenadas
def calcula_norma(nodo1, nodo2):
    return sqrt(pow((nodo2.x - nodo1.x), 2) + pow((nodo2.y - nodo1.y), 2))


def conectados(procurar):
    lista = []
    adjacentes = baseConhecimento.grafo1.get(procurar)
    for (local, dist) in adjacentes:
        lista.append(local)
    return lista


# Calcular distância
def calcula_distancia(nodos):
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


def caminho_to_string(cam: [Local]):
    caminho = "Caminho feito: "
    for nodo in cam:
        caminho = caminho + f"{nodo.nome} "

    return caminho
