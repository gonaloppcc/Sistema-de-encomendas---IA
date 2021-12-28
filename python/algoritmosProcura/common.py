# Funções para descobrir caminhos
# dfs, utilizando os slides PL(8) das aulas
import baseConhecimento


def conectados(procurar):
    lista = []
    adjacentes = baseConhecimento.distancias.get(procurar)
    for (local, dist) in adjacentes:
        lista.append(local)
    return lista


# Calcular distância
def calcula_distancia(listaNodos):
    total = 0
    for i in range(len(listaNodos) - 1):
        listaNodosConnectados = baseConhecimento.distancias[listaNodos[i]]
        for nome, dist in listaNodosConnectados:
            if nome.nome == listaNodos[i + 1].nome:
                total += dist
    return total

# Calcular tempos e velocidades a partir de entregas
def calcula_tempo_transporte(meioTransporte, pesoEncomenda, distância):
    velocidadeTransporte = meioTransporte.calculaVelocidade(pesoEncomenda)
    if velocidadeTransporte == 0:
        raise Exception("O meio de transporte não consegue levar a encomenda")
    return distância / velocidadeTransporte

def print_caminho(cam):
    for nodo in cam:
        print("Caminho: ", nodo.nome)
