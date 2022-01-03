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
    res = ""
    res += "Caminho: "
    for nodo in cam:
        res += nodo.nome
        res += " "

    return res


# Imprime pares que contêm o caminho e o id da encomenda que é entregue nessa encomenda.
# No caso de ser -1, é para voltar à base.
def print_caminho_pares(par, cidade_origem):
    cam, enc_id = par
    print("Cidade original: ", cidade_origem.id)
    print("Caminho para entregar encomenda: ", enc_id)
    for nodo in cam:
        print(nodo.nome)
    print()


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
