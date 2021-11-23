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


%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega -> {V,F}
entrega(2, carro, 1, rating, data(23/12/2019,18/40)).


%estafeta: id, nome, rating/num, cidade, nEncomendas -> {V,F}
estafeta(2, diogo, 4/420, povoaVarzim, 2).


%transporte: nome, pesoMaximo, velMax -> {V,F}
transporte(bicicleta, 5, 10).
transporte(moto, 20, 35).
transporte(carro, 100, 25).


%L = lista com pares(idEstafeta,Entregas).
l([
    1/[encomenda(2,qw,eqw,ads,asd,ads)],
    2/[encomenda(3,lkj,kink,ads,çoadj,123)]
  ]).

