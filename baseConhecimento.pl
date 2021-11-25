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
encomenda(2, 1, 20, 25, data(1,1,2), data(4,5,10), 1).
encomenda(3, 1, 20, 25, data(1,1,3), data(4,5,10), 1).
encomenda(4, 1, 21, 25, data(1,1,4), data(4,5,10), 1).

%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
entrega(2, carro, 1, rating, data(23,12,2019), hora(18,40)).
entrega(2, carro, 2, rating, data(23,12,2), hora(18,40)).
entrega(2, carro, 4, rating, data(23,12,2), hora(18,40)).
entrega(3, bicicleta, 3, rating, data(23,12,2039),hora(18,40)).

%estafeta: id, nome, rating/num, cidade, nEncomendas -> {V,F}
estafeta(3, banderas, 4/420, vilaDoConde, 1).
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
% Lista de encomendas
enc([
    encomenda(2,qw,eqw,ads,asd,ads, 4),
    encomenda(3,lkj,kink,ads,çoadj,123, 4)
  ]).
% Lista de entregas
entr([
    entrega(o,carro,1,w,1,a,b),
    entrega(w,carro,2,s,2,a,b),
    entrega(o,carro,1,w,1,a,b),
    entrega(d,moto,3,ad,3,a,b),
    entrega(as,bicicleta,2,s,2,a,b),
    entrega(oeqw,bicicleta,1,qw,1,a,b)
    ]).
% Lista de estafeta/entregas
esEnt(
[
  1/
    [
      entrega(1,carro,1,2,data(23,2,2021),a,3),
      entrega(1,carro,2,3,data(30,3,2021),b,c),
      entrega(1,bicicleta,3,2,data(4,4,2021),b,c),
      entrega(1,bicicleta,1,2,data(7,4,2021),b,c)
    ],
  2/
    [
      entrega(2,moto,2,4,s,b,c),
      entrega(2,moto,3,4,s,b,c),
      entrega(2,moto,2,5,s,b,c),
      entrega(2,bicicleta,1,4,d,b,c)
    ],
  3/
    [
      entrega(3,bicicleta,3,s,d,b,c),
      entrega(3,bicicleta,2,s,d,b,c),
      entrega(3,bicicleta,3,s,d,b,c),
      entrega(3,bicicleta,1,s,d,b,c),
      entrega(3,moto,2,ad,s,b,c)
    ]
]).
