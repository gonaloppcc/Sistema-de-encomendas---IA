import datetime

from base_conhecimento.Atribuicao import Atribuicao
from base_conhecimento.Encomenda import Encomenda
from base_conhecimento.Estafeta import Estafeta
from base_conhecimento.Local import Local
from base_conhecimento.Transporte import Transporte

# Conhecimento ------------------------------------------------------------


# Local: ID + Cidade + Nome da

# Locais da primeira fase
# TODO definir melhor as coordenadas

local1 = Local(1, "povoaVarzim", "local1", 76, 24)
local2 = Local(2, "vilaDoConde", "local2", 15, 104)
local3 = Local(3, "trofa", "avenida", 76, 7)
local4 = Local(4, "lisboa", "praca", 75, 130)

# Locais da segunda fase
local5 = Local(5, "grafo", "local5", 10, 14)
local6 = Local(6, "grafo", "local6", 39, 59)
local7 = Local(7, "grafo", "local7", 20, 76)
local8 = Local(8, "grafo", "local8", 45, 55)
local9 = Local(9, "grafo", "local9", 98, 33)
local10 = Local(10, "grafo", "local10", 16, 98)

# Map onde guardamos todas as ruas, por ‘id’.
locais = {
}
"""
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
"""

# Guarda as distâncias em função do ‘id’ da local
# Key é o ‘id’ da local, doutro lado temos ‘id’'s de outras locals, mais distâncias
# https://www.gatevidyalay.com/wp-content/uploads/2018/03/Dijkstra-Algorithm-Problem-01.png
grafo1 = {
}
"""
local5: [(local6, 1), (local7, 5)],
local6: [(local7, 2), (local8, 2), (local9, 1)],
local7: [(local9, 2)],
local8: [(local9, 3), (local10, 1)],
local9: [(local10, 2)],
local10: []
"""

# Constantes
# Map onde guardamos todas as origens em função das cidades, por nome.
# Assim, se quisermos procurar noutras cidades.
# Vamos procurar em que local está o centro de distribuição dessa cidade.
# E os estafetas saiem daí

origens = {
}
"""
"grafo": local5,
"""

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

# Transporte: Nome, peso Máximo possível transportar, velocidade máxima, descrescimento de velocidade, preço por km
bicicleta = Transporte("Bicicleta", 5, 10, 0.7, 5)
moto = Transporte("Moto", 20, 35, 0.5, 10)
carro = Transporte("Carro", 100, 25, 0.1, 20)
barco = Transporte("Barco", 20, 21, 0.6, 41)

transportes = [bicicleta, moto, carro, barco]

# Definição de uma encomenda
encomenda1 = Encomenda(1, 1, 20, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 10)
encomenda2 = Encomenda(2, 1, 80, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 9)

# Map onde guardamos todas as encomendas, por id.
encomendas = {
    1: encomenda1,
    2: encomenda2
}

estafeta1 = Estafeta(1, "marco", "grafo")

# Map onde guardamos todos os estafetas, por id.
estafetas = {
    1: estafeta1
}

# Nós aqui podemos dar o objeto inteiro, mas assim é mais limpo
atribuicao1 = Atribuicao(1, 1)
atribuicao2 = Atribuicao(1, 2)

# Lista onde guardamos todas as atribuições.
# Como só as consultamos sequencialmente, para gerar entregas, podem estar numa lista.
atribuicoes = [atribuicao1, atribuicao2]
