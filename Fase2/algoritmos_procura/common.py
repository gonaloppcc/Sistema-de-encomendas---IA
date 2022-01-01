# Funções para descobrir caminhos
# dfs, utilizando os diapositivos PL(8) das aulas
from base_conhecimento import baseConhecimento
from base_conhecimento.baseConhecimento import transportes


def conectados(procurar):
    lista = []
    adjacentes = baseConhecimento.distancias.get(procurar)
    for (local, dist) in adjacentes:
        lista.append(local)
    return lista


# Calcular distância
def calcula_distancia(nodos):
    total = 0
    for i in range(len(nodos) - 1):
        nodos_connectados = baseConhecimento.distancias[nodos[i]]
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


def print_caminho(cam):
    print("Caminho: ", end="")
    for nodo in cam:
        print(nodo.nome, end=" ")

    print()


# Calcual o máximo de peso que podemos levar numa dada viagem, a partir do máximo que os veículos podem transportar
def maximo_peso_uma_viagem():
    max = 0
    for veiculo in transportes:
        if veiculo.peso_maximo >= max:
            max = veiculo.peso_maximo
    return max
