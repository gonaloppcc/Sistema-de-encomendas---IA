from algoritmos_procura.bfs import bfs
from gera_encomendas.geraEntregas import gerar_entregas

# Descobrir caminho por algoritmo
"""
ori = baseConhecimento.local5
dest = baseConhecimento.local10

# Obtem um caminho em função da função utilizada
cam = dfs(ori, dest)

# Recebe um caminho, conjunto de nós, e calcula o custo total
print(ori.nome, " ", dest.nome)

if cam is not None:
    for nodo in cam:
        print("Caminho: ", nodo.nome)
else:
    print("Não há caminho")

print(" - ")

cam.reverse()

print_caminho(cam)
#Custo do caminho
distancia = calculaDistancia(cam)

print("O custo é: ", distancia)

#Velocidades, quanto maior o peso, maior o tempo
peso = 3
meioTransporte = baseConhecimento.bicicleta
print("Tempo de transporte do caminho com ", distancia, " é: ")
print(calculaTempoTransporte(meioTransporte, peso, distancia))
"""

# Gerar entregas
gerar_entregas(bfs)
