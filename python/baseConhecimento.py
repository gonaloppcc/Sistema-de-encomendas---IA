# Conhecimento ------------------------------------------------------------
#Base de conhecimento, o import não está a dar
class Rua:
    def __init__(self, id, freguesia, nome):
        self.id = id
        self.freguesia = freguesia
        self.nome = nome


#Ruas ID + Cidade + Nome da rua
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
#class Transporte:
 #Transportes e velocidade, temos tudo em Km/h
class Transporte:
    def __init__(self, nome, pesoMaximo, velocidadeMax, coeficienteKgVelocidade):
        self.nome = nome
        self.pesoMaximo = pesoMaximo
        self.velocidadeMax = velocidadeMax
        self.coeficienteKgVelocidade = coeficienteKgVelocidade
   
    def calculaVelocidade(self, pesoEncomenda):
        if pesoEncomenda > self.pesoMaximo: 
            return 0
        penalizaçãoPeso = self.coeficienteKgVelocidade * pesoEncomenda
        return self.velocidadeMax - penalizaçãoPeso
#transporte: nome, pesoMaximo, velMax -> {V,F}
#nós na fase 1 metemos 4 parâmetros, mas não sei o que é o último
# Nome, peso Máximo possível transportar, velocidade máxima, coeficiente peso/velocidade
bicicleta = Transporte("bicicleta", 5, 10, 0.7)
moto = Transporte("moto", 20, 35, 0.5)
carro = Transporte("carro", 100, 25, 0.1)
barco = Transporte("barco", 20, 21, 0.6)

   



"""

#TP1
#rua: id (equivalente ao nome do Nodo), freguesia, nome -> {V,F}
rua(2, povoaVarzim, rua1) 
rua(1, vilaDoConde, rua1)
rua(3, trofa,       avenida) 
rua(4, lisboa, praca)


#distancia: rua1, rua2 -> {V,F}
distancia(vilaDoConde, povoa_Varzim, 10)


#cliente: id, nome -> {V,F} 
cliente(1, marco)
cliente(2, diogo)
cliente(3, rita)
cliente(4, goncalo)
cliente(5, alice)

#encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, ruaID -> {V,F}. 
#Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
#                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 1, 20, 26, data(23,12,2019),     hora(14, 00), data(29,11, 2019),    hora(14, 00), 2)
encomenda(2, 2, 20, 25, data(23,12,2019),     hora(14, 00), data(29,11, 2019),   hora(14, 00), 1)
encomenda(3, 2, 20, 25, data(1,1,3),     hora(14, 00), data(4,5,10),   hora(14, 00), 3)
encomenda(4, 3, 21, 25, data(1,1,4),     hora(14, 00), data(4,5,10),   hora(14, 00), 1)
encomenda(5, 3, 21, 25, data(1,2,3),     hora(14, 00), data(4,5,10),   hora(14, 00), 1)
encomenda(6, 3, 21, 25, data(1,2,1),     hora(14, 00), data(4,5,10),   hora(14, 00), 3)
encomenda(7, 2, 10, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2)
encomenda(8, 2, 10, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2)
encomenda(9, 2, 70, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2)

#entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
#Não foram entregues 1
entrega(1, bicicleta,     1, 2, data(23,12,2019), hora(18,40))
entrega(1, bicicleta, 2, 5, data(23,12,2019), hora(19,00))
entrega(3, moto,      3, 4, data(23,12,2019), hora(19,20))
entrega(2, carro,     4, 4, data(23,12,2),    hora(18,40))
#entrega(1, moto,      4, 5, data(23,12,2),    hora(18,40))
entrega(4, bicicleta, 50, 5, data(23,12,2039), hora(18,40))
entrega(4, bicicleta, 6, 5, data(23,12,2039), hora(18,40))
entrega(2, bicicleta, 7, 1, data(23,12,2),    hora(18,40))
entrega(3, barco,     8, 3, data(30,10,2020), hora(23,10))

#atribuidos IdEstafeta, IdEncomenda
atribuido(1, 1)
#atribuido(3, 2)
#atribuido(1, 3)
atribuido(1, 4)
atribuido(4, 5)
atribuido(2, 6)
atribuido(1, 7)
atribuido(1, 8)
atribuido(1, 9)

#estafeta: id, nome, cidade -> {V,F}
estafeta(1, marco,      trofa)
estafeta(2, diogo,      povoaVarzim)
estafeta(5, banderitas, povoaVarzim)
estafeta(6, goncalo2,   povoaVarzim)
estafeta(3, banderas,   vilaDoConde)
estafeta(4, goncalo,    lisboa)

#transporte: nome, pesoMaximo, velMax -> {V,F}
transporte(bicicleta, 5,   10, 5)
transporte(moto,      20,  35, 10)
transporte(carro,     100, 25, 20)
transporte(barco,     20,  21, 41)

"""