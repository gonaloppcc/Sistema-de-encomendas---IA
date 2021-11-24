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
encomenda(2, 1, 20, 25, data(1,1,1), data(4,5,10), 1).
encomenda(3, 1, 20, 25, data(1,1,1), data(4,5,10), 1).
encomenda(4, 1, 21, 25, data(1,1,1), data(4,5,10), 1).


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
    entrega(o,carro,q,w,e),
    entrega(w,carro,q,s,d),
    entrega(o,carro,q,w,e),
    entrega(d,moto,s,ad,s),
    entrega(as,bicicleta,sa,s,d),
    entrega(oeqw,bicicleta,21,qw,d)
    ]).
% Lista de estafeta/entregas
esEnt(
[
  1/
    [
      entrega(1,carro,1,2,data(23,2,2021)),
      entrega(1,carro,5,3,data(30,3,2021)),
      entrega(1,bicicleta,7,2,data(4,4,2021)),
      entrega(1,bicicleta,8,2,data(7,4,2021))
    ],
  2/
    [
      entrega(2,moto,2,4,s),
      entrega(2,moto,4,4,s),
      entrega(2,moto,6,5,s),
      entrega(2,bicicleta,3,4,d)
    ],
  3/
    [
      entrega(3,bicicleta,sa,s,d),
      entrega(3,bicicleta,sa,s,d),
      entrega(3,bicicleta,sa,s,d),
      entrega(3,bicicleta,sa,s,d),
      entrega(3,moto,s,ad,s)
    ]
]).
