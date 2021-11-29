:- include('tempo.pl').

:- op( 900,xfy,'::' ).
:- dynamic encomenda/9.
:- dynamic entrega/6.
:- dynamic estafeta/3.
:- dynamic cliente/2.
:- dynamic transporte/4.
:- dynamic rua/3.
:- dynamic distancia/3.

+encomenda(EncID,Cliente,Peso,Volume,Prazo,HoraEnt,DataEnc,HoraEnc,Rua) :: 
(    
    findall(EncID,encomenda(EncID,_,_,_,_,_,_,_,_),R),
    length(R,L),
    L == 1,
    cliente(Cliente,_),
    Peso > 0,
    Volume > 0,
    Prazo,
    HoraEnt,
    DataEnc,
    HoraEnc,
    rua(Rua,_,_) 
).

+entrega(IDEstafeta,Veiculo,EncID,Data,Hora,Rua) ::
(
    findall(EncID,entrega(_,_,EncID,_,_,_),R),
    length(R,L),
    L == 1,
    estafeta(IDEstafeta,_,_,_,_),
    encomenda(EncID,_,_,_,_,_,_),
    transporte(Veiculo,_,_),
    Data,
    Hora,
    rua(Rua,_,_)
).

+estafeta(ID,_,_) ::
(
    findall(ID,estafeta(ID,_,_),R),
    length(R,L),
    L == 1
).

+transporte(Veiculo,Carga,Velocidade,Preco) ::
(
    findall(Veiculo,transporte(Veiculo,_,_),R),
    length(R,L),
    L == 1,
    Carga > 0,
    Velocidade > 0,
    Preco > 0
).

+cliente(ID,_) ::
(
    findall(ID,cliente(ID,_),R),
    length(R,L),
    L == 1
). 

+rua(ID,_,_) ::
(
    findall(ID, rua(ID,_,_),R),
    length(R,L),
    L == 1
).

evolucao( Termo ) :- 
    findall(Invariante,+Termo::Invariante,Lista),
    insercao(Termo),
    teste(Lista)
.

insercao(Termo) :- assert(Termo).
insercao(Termo) :- retract(Termo),!,fail.

teste([]).
teste([H|T]) :- H, teste(T).

%rua: id, freguesia, nome -> {V,F}
rua(1, vilaDoConde, rua1). 
rua(2, povoaVarzim, rua1). 


%distancia: rua1, rua2 -> {V,F}
distancia(vilaDoConde, povoa_Varzim, 10). 


%cliente: id, nome -> {V,F} 
cliente(1, marco).


%encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, ruaID -> {V,F}. 
%Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
%                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 1, 20, 25, data(1,1,1), hora(14, 00), data(4,5,1), hora(14, 00), 2).
encomenda(2, 2, 20, 25, data(1,1,2), hora(14, 00), data(4,5,10), hora(14, 00), 1).
encomenda(3, 2, 20, 25, data(1,1,3), hora(14, 00), data(4,5,10), hora(14, 00), 3).
encomenda(4, 3, 21, 25, data(1,1,4), hora(14, 00), data(4,5,10), hora(14, 00), 1).
encomenda(5, 3, 21, 25, data(1,2,3), hora(14, 00), data(4,5,10), hora(14, 00), 1).
encomenda(6, 3, 21, 25, data(1,2,1), hora(14, 00), data(4,5,10), hora(14, 00), 1).
encomenda(7, 3, 21, 25, data(1,2,1), hora(14, 00), data(4,5,10), hora(14, 00), 1).

%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
%Não foram entregues 1
entrega(1, carro, 1, 2, data(23,12,2019), hora(18,40)).
entrega(1, bicicleta, 3, rating, data(23,12,2019), hora(19,00)).
entrega(3, mota, 2, 4, data(23,12,2019), hora(19,20)).
%entrega(2, carro, 3, 4, data(23,12,2), hora(18,40)).
entrega(1, moto, 4, 5, data(23,12,2), hora(18,40)).
entrega(4, bicicleta, 5, 5, data(23,12,2039),hora(18,40)).
entrega(2, bicicleta, 6, 1, data(23,12,2),hora(18,40)).

%estafeta: id, nome, cidade -> {V,F}
estafeta(1, marco, trofa).
estafeta(2, diogo, povoaVarzim).
estafeta(3, banderas, vilaDoConde).
estafeta(4, goncalo, lisboa).

%transporte: nome, pesoMaximo, velMax -> {V,F}
transporte(bicicleta, 5, 10, 5).
transporte(moto, 20, 35, 10).
transporte(carro, 100, 25, 20).

