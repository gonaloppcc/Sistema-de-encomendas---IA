from base_conhecimento.Estafeta import Estafeta
from base_conhecimento.Local import Local
from base_conhecimento.Transporte import Transporte

# Conhecimento ------------------------------------------------------------


# Local: ID + Cidade + Nome da

# Locais da primeira fase
# TODO definir melhor as coordenadas

local0 = Local(0, "Vila do Conde", "local1", 76, 24)
local1 = Local(1, "Vila do Conde", "local2", 15, 104)
local2 = Local(2, "Vila do Conde", "avenida", 76, 7)
local3 = Local(3, "Vila do Conde", "praça", 75, 130)

# Locais da segunda fase
local4 = Local(4, "Vila do Conde", "local5", 10, 14)
local5 = Local(5, "Vila do Conde", "local6", 39, 59)
local6 = Local(6, "Vila do Conde", "local7", 20, 76)
local7 = Local(7, "Vila do Conde", "local8", 45, 55)
local8 = Local(8, "Vila do Conde", "local9", 98, 33)
local9 = Local(9, "Vila do Conde", "local10", 16, 98)

# Guarda as distâncias em função do ‘id’ da local
# Key é o ‘id’ da local, doutro lado temos ‘id’'s de outras locals, mais distâncias
# https://www.gatevidyalay.com/wp-content/uploads/2018/03/Dijkstra-Algorithm-Problem-01.png
mapa = {
    "grafos": {
        "Vila do Conde": {
            local4: [(local5, 1), (local6, 5)],
            local5: [(local6, 2), (local7, 2), (local8, 1)],
            local6: [(local8, 2)],
            local7: [(local8, 3), (local9, 1)],
            local8: [(local9, 2), (local4, 3)],
            local9: [(local4, 4)]
        }
    },
    "id_counter": 10
}

# Guarda os ids dos locais que pertencem a cada cidade, útil para gerarmos as encomendas.
id_locais_cidades = {
    "Vila do Conde": (4, 10)
}

"""
 circuito : (counter, peso, volume, entregas)
 circuito -> String do circuito
 counter  -> Nº de vezes que o percurso foi feito
 peso     -> Peso total de todas as entregas feitas neste percurso
 volume   -> Volume total de todas as entregas feitas neste percurso
 entregas -> Lista de listas de entregas
"""
circuitos_efetuados = {}

# Constantes
# Map onde guardamos todas as origens em função das cidades, por nome.
# Assim, se quisermos procurar noutras cidades.
# Vamos procurar em que local está o centro de distribuição dessa cidade.
# E os estafetas saiem daí

origens = {
    "Vila do Conde": local4
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

# Transporte: Nome, peso Máximo possível transportar, velocidade máxima, descrescimento de velocidade, preço por km
bicicleta = Transporte("bicicleta", 5, 10, 0.7, 5, 0)
moto = Transporte("moto", 25, 35, 0.5, 10, 0.5)
carro = Transporte("carro", 100, 25, 0.1, 20, 1)
barco = Transporte("barco", 20, 21, 0.6, 41, 0.4)

transportes = [bicicleta, moto, carro, barco]

# Definição de uma encomenda
"""
encomenda1 = Encomenda(1, 1, 5, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 10)
encomenda2 = Encomenda(2, 1, 101, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 9)
encomenda3 = Encomenda(2, 1, 16, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 8)
encomenda4 = Encomenda(2, 1, 20, 26, datetime.datetime(2020, 5, 20), datetime.datetime(2020, 5, 17), 7)
"""
# Map onde guardamos todas as encomendas, por id.
encomendas = {

}

estafeta1 = Estafeta(1, "diogo", "Vila do Conde")
# Map onde guardamos todos os estafetas, por cidade. Assumimos que só existe um estafeta por cidade.
estafetas = {
    "Vila do Conde": estafeta1
}

# Nós aqui podemos dar o objeto inteiro, mas assim é mais limpo
# Estafeta id, encomenda id.
"""
atribuicao1 = Atribuicao(1, 1)
atribuicao2 = Atribuicao(1, 2)

atribuicao3 = Atribuicao(1, 3)
atribuicao4 = Atribuicao(2, 3)
"""
# Onde guardamos as entregas realizadas.
entregas = []

# Lista onde guardamos todas as atribuições.
# Como só as consultamos sequencialmente, para gerar entregas, podem estar numa lista.
atribuicoes = []
