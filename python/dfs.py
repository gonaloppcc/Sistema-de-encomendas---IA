import baseConhecimento

#Funções para descobrir caminhos
#dfs, utilizando os slides PL(8) das aulas
def conectados(procurar):
    lista = []
    adjacentes = baseConhecimento.distancias.get(procurar)
    for (rua, dist) in adjacentes:
        lista.append(rua)
    return lista

def dfs2(origem, destino, listaAtual):
    #Caso chegue ao destino certo
    if origem == destino:
        return listaAtual
    #Caso seja um dead-end
    if origem not in baseConhecimento.distancias:
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
    ruas = baseConhecimento.distancias.keys()
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
        listaNodosConnectados = baseConhecimento.distancias[listaNodos[i]]
        for nome, dist in listaNodosConnectados:
            if nome.nome==listaNodos[i+1].nome: 
                total+=dist
    return total

ori = baseConhecimento.ruaTP2_1
dest = baseConhecimento.ruaTP2_6
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
        

#Calcular tempos e velocidades a partir de entregas

def calculaTempoTransporte(meioTransporte, pesoEncomenda, distância):
    velocidadeTransporte = meioTransporte.calculaVelocidade(pesoEncomenda)
    if velocidadeTransporte == 0: 
        raise Exception("O meio de transporte não consegue levar a encomenda")
    return distância / velocidadeTransporte

peso = 0
meioTransporte = baseConhecimento.bicicleta    
print("Tempo de transporte do caminho com ", distancia, " é: ")
print(calculaTempoTransporte(meioTransporte, peso, distancia))










#Só para aprender, não funciona bem
def distancia(ruaDest):
    lista = distancias.get(origem)
    for (nodoOrigem, nodoDestino) in lista:
        print(nodoOrigem.nome, " ", nodoDestino)
    for (nodoOrigem, nodoDestino) in lista:
            if nodoOrigem == ruaDest:
                print("Encontrou ", origem.nome , ruaDest.nome)

