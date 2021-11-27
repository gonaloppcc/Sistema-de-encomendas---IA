%rua: id, freguesia, nome -> {V,F}
rua(1, vilaDoConde, rua1). 
rua(2, povoaVarzim, rua1). 


%distancia: rua1, rua2 -> {V,F}
distancia(vilaDoConde, povoa_Varzim, 10). 


%cliente: id, nome -> {V,F} 
cliente(1, marco).


%encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, dataDeEncomenda, ruaID -> {V,F}. 
%Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
%                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 1, 20, 25, data(1,1,1), data(4,5,1), 2).
encomenda(2, 2, 20, 25, data(1,1,2), data(4,5,10), 1).
encomenda(3, 2, 20, 25, data(1,1,3), data(4,5,10), 3).
encomenda(4, 3, 21, 25, data(1,1,4), data(4,5,10), 1).
encomenda(5, 3, 21, 25, data(1,2,3), data(4,5,10), 1).
encomenda(6, 3, 21, 25, data(1,2,1), data(4,5,10), 1).

%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
entrega(1, carro, 1, rating, data(23,12,2019), hora(18,40)).
entrega(1, bicicleta, 3, rating, data(23,12,2019), hora(19,00)).
entrega(1, mota, 2, rating, data(23,12,2019), hora(19,20)).
entrega(2, carro, 2, rating, data(23,12,2), hora(18,40)).
entrega(1, moto, 3, rating, data(23,12,2), hora(18,40)).
entrega(4, bicicleta, 4, rating, data(23,12,2039),hora(18,40)).
entrega(2, bicicleta, 5, rating, data(23,12,2),hora(18,40)).

%estafeta: id, nome, rating/num, cidade, nEncomendas -> {V,F}
estafeta(3, banderas, 4/420, vilaDoConde, 1).
estafeta(2, diogo, 4/420, povoaVarzim, 2).


%transporte: nome, pesoMaximo, velMax -> {V,F}
transporte(bicicleta, 5, 10).
transporte(moto, 20, 35).
transporte(carro, 100, 25).

