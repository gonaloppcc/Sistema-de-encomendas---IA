# Conhecimento ------------------------------------------------------------
# Base de conhecimento, o import não está a dar
class Local:
    def __init__(self, id, freguesia, nome):
        self.id = id
        self.freguesia = freguesia
        self.nome = nome


# Local: ID + Cidade + Nome da

# Local da primeira fase
local1 = Local(2, "povoaVarzim", "local1")
local2 = Local(1, "vilaDoConde", "local1")
local3 = Local(3, "trofa", "avenida")
local4 = Local(4, "lisboa", "praca")

# Local da segunda fase
local5 = Local(1, "grafo", "localTP2_1")
local6 = Local(2, "grafo", "localTP2_2")
local7 = Local(3, "grafo", "localTP2_3")
local8 = Local(4, "grafo", "localTP2_4")
local9 = Local(5, "grafo", "localTP2_5")
local10 = Local(6, "grafo", "localTP2_6")

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
origem = local5

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
    def __init__(self, nome, pesoMaximo, velocidadeMax, coeficienteKgVelocidade, precoKm):
        self.nome = nome
        self.pesoMaximo = pesoMaximo
        self.velocidadeMax = velocidadeMax
        self.coeficienteKgVelocidade = coeficienteKgVelocidade
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
