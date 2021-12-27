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
def calculaDistancia(listaNodos):
    print("Caminho começa")
    print(listaNodos)
    total = 0
    for i in range(len(listaNodos) - 1):
        listaNodosConnectados = baseConhecimento.distancias[listaNodos[i]]
        for nome, dist in listaNodosConnectados:
            print("Só nome e outro ", nome.nome, " ", listaNodos[i + 1].nome)
        for nome, dist in listaNodosConnectados:
            if nome.nome == listaNodos[i + 1].nome:
                print("Segundo print: ", nome.nome)
                total += dist
    return total

# Calcular tempos e velocidades a partir de entregas
def calculaTempoTransporte(meioTransporte, pesoEncomenda, distância):
    velocidadeTransporte = meioTransporte.calculaVelocidade(pesoEncomenda)
    if velocidadeTransporte == 0:
        raise Exception("O meio de transporte não consegue levar a encomenda")
    return distância / velocidadeTransporte
