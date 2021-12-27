import baseConhecimento
from algoritmosProcura.common import calculaDistancia, calculaTempoTransporte
from algoritmosProcura.dfs import dfs

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

for nodo in cam:
    print("Reverso: ", nodo.nome)

distancia = calculaDistancia(cam)

print("O custo é: ", distancia)


peso = 0
meioTransporte = baseConhecimento.bicicleta
print("Tempo de transporte do caminho com ", distancia, " é: ")
print(calculaTempoTransporte(meioTransporte, peso, distancia))
