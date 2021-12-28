import datetime


# Conhecimento ------------------------------------------------------------
# Base de conhecimento, o import não está a dar
class Local:
    def __init__(self, id, freguesia, nome):
        self.id = id
        self.freguesia = freguesia
        self.nome = nome


# Local: ID + Cidade + Nome da

# Local da primeira fase
local1 = Local(1, "povoaVarzim", "local1")
local2 = Local(2, "vilaDoConde", "local1")
local3 = Local(3, "trofa", "avenida")
local4 = Local(4, "lisboa", "praca")

# Local da segunda fase
local5 = Local(5, "grafo", "localTP2_1")
local6 = Local(6, "grafo", "localTP2_2")
local7 = Local(7, "grafo", "localTP2_3")
local8 = Local(8, "grafo", "localTP2_4")
local9 = Local(9, "grafo", "localTP2_5")
local10 = Local(10, "grafo", "localTP2_6")

# Map onde guardamos todas as ruas, por id.
locais = {
    1: local1,
    2: local2,
    3: local3,
    4: local4,
    5: local5,
    6: local6,
    7: local7,
    8: local8,
    9: local9,
    10: local10,
}

# Guarda as distâncias em função do id da local
# Key é o ‘id’ da local, outro lado temos id's de outras locals, mais distâncias
# https://www.gatevidyalay.com/wp-content/uploads/2018/03/Dijkstra-Algorithm-Problem-01.png
distancias = {
    local5: [(local6, 1), (local7, 5)],
    local6: [(local7, 2), (local8, 2), (local9, 1)],
    local7: [(local9, 2)],
    local8: [(local9, 3), (local10, 1)],
    local9: [(local10, 2)],
    local10: []
}

# Constantes
# Map onde guardamos todas as origens em função das cidades, por nome.
#Assim, se quisermos procurar noutras cidades.
# vamos procurar em que local está o centro de distribuição dessa cidade.
#E os estafetas saiem daí

origens = {
    "grafo": local5,
}

"""
1-> 2 (1), 3 (5)
2 -> 3 (2), 4 (2), 5 (1)
3 -> 5 (2)
4 -> 5 (3), 6 (1)
5 -> 6 (2) 

   2  >  4
1  ↓     ↓   6
   3  >  5

"""


# Class Transporte:
# Transportes e velocidade, temos tudo em Km/h
class Transporte:
    def __init__(self, nome, pesoMaximo, velocidadeMax, coeficiente_Kg_velocidade, precoKm):
        self.nome = nome
        self.pesoMaximo = pesoMaximo
        self.velocidadeMax = velocidadeMax
        self.coeficienteKgVelocidade = coeficiente_Kg_velocidade
        self.precoKm = precoKm

    def calculaVelocidade(self, pesoEncomenda):
        if pesoEncomenda > self.pesoMaximo:
            return 0
        penalizacaoPeso = self.coeficienteKgVelocidade * pesoEncomenda
        return self.velocidadeMax - penalizacaoPeso


# Transporte: Nome, peso Máximo possível transportar, velocidade máxima, descrescimento de velocidade, preço por km
bicicleta = Transporte("bicicleta", 5, 10, 0.7, 5)
moto = Transporte("moto", 20, 35, 0.5, 10)
carro = Transporte("carro", 100, 25, 0.1, 20)
barco = Transporte("barco", 20, 21, 0.6, 41)

transportes = [bicicleta, moto, carro, barco]

# Encomendas
# Usamos o tipo de dados Data de pyhton, juntando dias e horas
# encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, localID -> {V,F}.
class Encomenda:
    def __init__(self, encomenda_id, cliente_id, peso, volume, prazo, data_encomenda, id_local_entrega):
        self.encomenda_id = encomenda_id
        self.cliente_id = cliente_id
        self.peso = peso
        self.volume = volume
        self.prazo = prazo
        self.data_encomenda = data_encomenda
        self.id_local_entrega = id_local_entrega


# Definição de uma encomenda
encomenda1 = Encomenda(1, 1, 20, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 10)
encomenda2 = Encomenda(2, 1, 80, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 9)

# Map onde guardamos todas as encomendas, por id.
encomendas = {
    1: encomenda1,
    2: encomenda2
}


# Estafetas
# São caraterizados por um ID, um nome, e um posto de distribuição, cidade.
# A cidade é uma string, e é o segundo parâmetro de um Local
class Estafeta:
    def __init__(self, estafeta_id, nome, cidade):
        self.estafeta_id = estafeta_id
        self.nome = nome
        self.cidade = cidade
    # Este estafeta entrega no grafo atual


estafeta1 = Estafeta(1, "marco", "grafo")

# Map onde guardamos todos os estafetas, por id.
estafetas = {
    1: estafeta1
}


# Atribuições, de um estafeta a uma encomenda
class Atribuicao:
    def __init__(self, estafeta_id, encomenda_id):
        self.estafeta_id = estafeta_id
        self.encomenda_id = encomenda_id


# Nós aqui podemos dar o objeto inteiro, mas assim é mais limpo
atribuicao1 = Atribuicao(1, 1)
atribuicao2 = Atribuicao(1, 2)

# Lista onde guardamos todas as atribuições.
# Como só as consultamos sequencialmente, para gerar entregas, podem estar numa lista.
atribuicoes = [atribuicao1, atribuicao2]
