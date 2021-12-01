:- include('tempo.pl').

:- op( 900,xfy,'::' ).
:- dynamic encomenda/9.
:- dynamic entrega/6.
:- dynamic estafeta/3.
:- dynamic cliente/2.
:- dynamic transporte/4.
:- dynamic rua/3.
:- dynamic distancia/3.
:- dynamic atribuido/2.

% Invariantes -------------------------------------------------------------
% Encomenda ---------------------------------------------------------------
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
-encomenda(EncID,_,_,_,_,_,_,_,_) :: 
(
    \+ entrega(_,_,EncID,_,_,_),
    \+ atribuido(_,EncID)
).

% Entrega -----------------------------------------------------------------
+entrega(IDEstafeta,Veiculo,EncID,Rating,Data,Hora) :: 
(
    findall(EncID,(entrega(_,_,EncID,_,_,_)),R),
    length( R,N ),
	N == 1,
    estafeta(IDEstafeta,_,_),
    encomenda(EncID,_,_,_,_,_,_,_,_),
    transporte(Veiculo,_,_,_),
    atribuido(IDEstafeta,EncID),
    Rating >= 0,
    Rating =< 5,
    Data,
    Hora
).
-entrega(_,_,_,_,_,_) :: (true). % Como não há outro facto que dependa deste podemos remove-lo sempre

% Estafeta ----------------------------------------------------------------
+estafeta(ID,_,_) ::
(
    findall(ID,estafeta(ID,_,_),R),
    length(R,L),
    L == 1
).
-estafeta(ID,_,_) ::
(
    \+ entrega(ID,_,_,_,_,_),
    \+ atribuido(ID,_)
).

% Transporte --------------------------------------------------------------
+transporte(Veiculo,Carga,Velocidade,Preco) ::
(
    findall(Veiculo,transporte(Veiculo,_,_),R),
    length(R,L),
    L == 1,
    Carga > 0,
    Velocidade > 0,
    Preco > 0
).
-transporte(Veiculo,_,_,_) ::
(
    \+ entrega(_,Veiculo,_,_,_,_)
).

% Cliente -----------------------------------------------------------------
+cliente(ID,_) ::
(
    findall(ID,cliente(ID,_),R),
    length(R,L),
    L == 1
). 
-cliente(ID,_) ::
(
    \+ encomenda(_,ID,_,_,_,_,_,_,_)
).

% Rua ---------------------------------------------------------------------
+rua(ID,_,_) ::
(
    findall(ID, rua(ID,_,_),R),
    length(R,L),
    L == 1
).
-rua(ID,_,_) ::
(
    \+ encomenda(_,_,_,_,_,_,_,_,ID)
).

% Atribuido ---------------------------------------------------------------
+atribuido(Estafeta, EncID) ::
(
    findall(EncID, atribuido(_,EncID), R),
    length(R,N),
    N == 1,
    estafeta(Estafeta,_,_),
    encomenda(EncID,_,_,_,_,_,_,_,_)
).
-atribuido(Estafeta,EncID) ::
(
    \+ entrega(_,_,EncID,_,_,_)
).

% Predicados de adição/remoção de conhecimento ----------------------------
evolucao( Termo ) :- 
    findall(Invariante,+Termo::Invariante,Lista),
    insercao(Termo),
    teste(Lista)
. 

remove(Termo) :-
    findall(Invariante,-Termo::Invariante,Lista),
    teste(Lista),
    remocao(Termo)
.

insercao(Termo) :- assert(Termo).
insercao(Termo) :- retract(Termo),!,fail.

remocao(Termo) :- retract(Termo).

teste([]).
teste([H|T]) :- H, teste(T).

% Conhecimento ------------------------------------------------------------
%rua: id, freguesia, nome -> {V,F}
rua(1, vilaDoConde, rua1). 
rua(2, povoaVarzim, rua1). 
rua(3, trofa,       avenida). 
rua(4, braga,       rua4).


%distancia: rua1, rua2 -> {V,F}
distancia(vilaDoConde, povoa_Varzim, 10). 


%cliente: id, nome -> {V,F} 
cliente(1, marco).
cliente(2, diogo).
cliente(3, rita).
cliente(4, goncalo).
cliente(5, alice).

%encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, ruaID -> {V,F}. 
%Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
%                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 1, 20, 25, data(23,12,2019),     hora(14, 00), data(4,5,1),    hora(14, 00), 2).
encomenda(2, 2, 20, 25, data(23,12,2019),     hora(14, 00), data(4,5,10),   hora(14, 00), 1).
encomenda(3, 2, 20, 25, data(1,1,3),     hora(14, 00), data(4,5,10),   hora(14, 00), 3).
encomenda(4, 3, 21, 25, data(1,1,4),     hora(14, 00), data(4,5,10),   hora(14, 00), 1).
encomenda(5, 3, 21, 25, data(1,2,3),     hora(14, 00), data(4,5,10),   hora(14, 00), 1).
encomenda(6, 3, 21, 25, data(1,2,1),     hora(14, 00), data(4,5,10),   hora(14, 00), 3).
encomenda(7, 2, 10, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2).
encomenda(8, 2, 10, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2).
encomenda(9, 2, 70, 5,  data(12,3,2020), hora(15,40),  data(5,2,2020), hora(9,10), 2).

%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
%Não foram entregues 1
entrega(1, bicicleta,     1, 2, data(23,12,2019), hora(18,40)).
entrega(1, bicicleta, 2, 5, data(23,12,2019), hora(19,00)).
entrega(3, moto,      3, 4, data(23,12,2019), hora(19,20)).
entrega(2, carro,     4, 4, data(23,12,2),    hora(18,40)).
%entrega(1, moto,      4, 5, data(23,12,2),    hora(18,40)).
entrega(4, bicicleta, 6, 5, data(23,12,2039), hora(18,40)).
entrega(2, bicicleta, 7, 1, data(23,12,2),    hora(18,40)).

%atribuidos IdEstafeta, IdEncomenda
atribuido(1, 1).
atribuido(3, 2).
atribuido(1, 3).
atribuido(1, 4).
atribuido(4, 6).
atribuido(2, 6).
atribuido(1, 7).
atribuido(1, 8).
atribuido(1, 9).

%estafeta: id, nome, cidade -> {V,F}
estafeta(1, marco,      trofa).
estafeta(2, diogo,      povoaVarzim).
estafeta(5, banderitas, povoaVarzim).
estafeta(6, gonçalo2,   povoaVarzim).
estafeta(3, banderas,   vilaDoConde).
estafeta(4, goncalo,    lisboa).

%transporte: nome, pesoMaximo, velMax -> {V,F}
transporte(bicicleta, 5,   10, 5).
transporte(moto,      20,  35, 10).
transporte(carro,     100, 25, 20).
transporte(barco,20,21,41).

