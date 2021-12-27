#import baseConhecimento

#Base de conhecimento, o import não está a dar
class Rua:
    def __init__(self, id, freguesia, nome):
        self.id = id
        self.freguesia = freguesia
        self.nome = nome


#Ruas
ruaTP1_1 = Rua(2, "povoaVarzim", "rua1")
ruaTP1_2 = Rua(1, "vilaDoConde", "rua1")
ruaTP1_3 = Rua(3, "trofa", "avenida")
ruaTP1_4 = Rua(4, "lisboa", "praca")

ruaTP2_1 = Rua(1, "grafo", "ruaTP2_1" )
ruaTP2_2 = Rua(2, "grafo", "ruaTP2_2" )
ruaTP2_3 = Rua(3, "grafo", "ruaTP2_3" )
ruaTP2_4 = Rua(4, "grafo", "ruaTP2_4" )
ruaTP2_5 = Rua(5, "grafo", "ruaTP2_5" )
ruaTP2_6 = Rua(6, "grafo", "ruaTP2_6" )
#Guarda as cidades de cada rua
#id , cidade/freguesia, nome
ruasCidades = { ruaTP1_1, ruaTP1_2, 
                ruaTP1_3, ruaTP1_4, 

                ruaTP2_1, ruaTP2_2, ruaTP2_3, 
                ruaTP2_4, ruaTP2_5, ruaTP2_6
              }

#Guarda as distâncias em função do id da rua
# Key é o id da rua, outro lado temos id's de outras ruas, mais distâncias
#https://www.gatevidyalay.com/wp-content/uploads/2018/03/Dijkstra-Algorithm-Problem-01.png

distancias = {
    ruaTP2_1 : [(ruaTP2_2, 1), (ruaTP2_3, 5)],
    ruaTP2_2 : [(ruaTP2_3, 2), (ruaTP2_4, 2), (ruaTP2_5, 1)],
    ruaTP2_3 : [(ruaTP2_5, 2)],
    ruaTP2_4 : [(ruaTP2_5, 3), (ruaTP2_6, 1)],
    ruaTP2_5 : [(ruaTP2_6, 2)],
    ruaTP2_6 : []
}

#Constantes
origem = ruaTP2_1

#Funções
#dfs, utilizando os slides PL(8) das aulas
def conectados(procurar):
    lista = []
    adjacentes = distancias.get(procurar)
    for (rua, dist) in adjacentes:
        lista.append(rua)
    return lista

def dfs2(origem, destino, listaAtual):
    #Caso chegue ao destino certo
    if origem == destino:
        return listaAtual
    #Caso seja um dead-end
    if origem not in distancias:
        return None
    ligados = conectados(origem)
    #Vamos guardar todos os caminhos não nulos
    #Por cada nó ligado ao atual
    for umNó in ligados:
        #Se o nó não tiver sido já visitado
        if umNó not in listaAtual:
            #Temos de guardar a lista porque, caso o dfs2 chegue a um dead-end
            #Temos de continuar a procurar, equivalente a backtrace
            listaAntesAlterar = listaAtual.copy()
            #Insere à cabeçaporque procuramos sempre o primeiro elemento da lista
            listaAtual.insert(0, umNó)

            #Chamada recursiva
            resRec = dfs2(umNó, destino,listaAtual)
            #Se der nulo, caminho não vai onde queremos, voltamos atrás
            #Caso contrário, retornamos o caminho válido
            if resRec is not None: return resRec
            else: #Equivale ao backtrace
                listaAtual = listaAntesAlterar

def dfs(origem, destino):
    return dfs2(origem, destino, [origem])

#bfs 
#Travessia de grafos, mas usei outro algoritmo

def bfs(origem, destino):
    #Guardamos os pares (nó atual, caminho até ele)
    queue = [(origem,[origem])]
    #Inicializamos todos os nodos como não visitados, num Map
    visitados = {}
    ruas = distancias.keys()
    for umaKey in ruas:
        visitados[umaKey] = False

    while queue:
        vertex, path = queue.pop(0)
        visitados[vertex] = True
        #Por cada nó adjacente ao atual, temos de o verificar
        for node in conectados(vertex):
            #Se o nó for o destino, devolvemos o caminho até ao "node" mais o próprio node
            if node == destino:
                return path + [destino]
            else:
                #Se o nó não foi visitado, adicionamos o nó atual à queue, com o caminho até ele
                if visitados[node] == False:
                    visitados[node] = True 
                    queue.append((node, path + [node]))

#Busca Iterativa Limitada em Profundidade. 
#Eu fiz como diz no slide: T(5) Classical Search
#Este método Pesquisa em Profundidade Iterativa 
def dfsLimited2(origem, destino, listaAtual, nivelAtual):
    if nivelAtual == 0:
        return None    
    #Caso chegue ao destino certo
    if origem == destino:
        return listaAtual
    #Caso seja um dead-end
    if origem not in distancias:
        return None
    #Nós adjacentes ao atual (origem)
    ligados = conectados(origem)
    #Vamos guardar todos os caminhos não nulos
    #Por cada nó ligado ao atual
    for umNó in ligados:
        #Se o nó não tiver sido já visitado
        if umNó not in listaAtual:
            #Temos de guardar a lista porque, caso o dfs2 chegue a um dead-end
            #Temos de continuar a procurar, equivalente a backtrace
            listaAntesAlterar = listaAtual.copy()
            #Insere à cabeçaporque procuramos sempre o primeiro elemento da lista
            listaAtual.insert(0, umNó)

            #Chamada recursiva
            resRec = dfsLimited2(umNó, destino,listaAtual, nivelAtual-1)
            #Se der nulo, caminho não vai onde queremos, voltamos atrás
            #Caso contrário, retornamos o caminho válido
            if resRec is not None: return resRec
            else: #Equivale ao backtrace
                listaAtual = listaAntesAlterar
    return None


def dfsLimited(origem, destino):
    #Tenta procurar uma solução em cada nível
    lista = None
    nivelAtual = 1
    while lista == None:
        #Se a lista contiver algo, sai do ciclo
        lista = dfsLimited2(origem, destino, [origem],nivelAtual)
        nivelAtual+=1
    return lista.reverse()

#Calcular distância
def calculaDistancia(listaNodos):
    print("Caminho começa")
    print(listaNodos)
    total = 0
    for i in range(len(listaNodos)-1):
        listaNodosConnectados = distancias[listaNodos[i]]
        for nome, dist in listaNodosConnectados:
            print("Só nome e outro ",nome.nome, " ", listaNodos[i+1].nome )
        for nome, dist in listaNodosConnectados:
            if nome.nome==listaNodos[i+1].nome: 
                print("Segundo print: ", nome.nome)
                total+=dist
    return total

ori = ruaTP2_1
dest = ruaTP2_6
#Obtem um caminho em função da função utilizada
cam = dfs(ori,dest)
#Recebe um caminho, conjunto de nós, e calcula o custo total
print(ori.nome, " ", dest.nome)
if cam is not None:
    for nodo in cam:
        print("Caminho: ", nodo.nome)
else: print("Não há caminho")
print(" - ")
cam.reverse()
for nodo in cam:
    print("Reverso: ", nodo.nome)
distancia = calculaDistancia(cam)
print("O custo é: ", distancia)
        
#Só para aprender, não funciona bem
def distancia(ruaDest):
    lista = distancias.get(origem)
    for (nodoOrigem, nodoDestino) in lista:
        print(nodoOrigem.nome, " ", nodoDestino)
    for (nodoOrigem, nodoDestino) in lista:
            if nodoOrigem == ruaDest:
                print("Encontrou ", origem.nome , ruaDest.nome)

