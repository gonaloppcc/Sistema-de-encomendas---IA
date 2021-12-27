#TP1
#local: id (equivalente ao nome do Nodo), freguesia, nome -> {V,F}
local(2, povoaVarzim, local1)
local(1, vilaDoConde, local1)
local(3, trofa,       avenida)
local(4, lisboa, praca)


#distancia: local1, local2 -> {V,F}
distancia(vilaDoConde, povoa_Varzim, 10)


#cliente: id, nome -> {V,F}
cliente(1, marco)
cliente(2, diogo)
cliente(3, rita)
cliente(4, goncalo)
cliente(5, alice)

#encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, localID -> {V,F}.
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

#transporte: nome, pesoMaximo, velMax, preco por km -> {V,F}
transporte(bicicleta, 5,   10, 5)
transporte(moto,      20,  35, 10)
transporte(carro,     100, 25, 20)
transporte(barco,     20,  21, 41)