% Objetivo da Empresa Green Distribution -> Privilegiar sempre o meio de transporte + ecológico

% Todos os ids usados devem ser únicos! De forma a que a unificação só ocorra uma vez no maximo para um id.

:- include('baseConhecimento.pl').
:- include('tempo.pl').

%Atribuir ratings
estafetaEntregaSucesso(estafeta(Id, Nome, 5), estafeta(Id, Nome, 5)):- !.
estafetaEntregaSucesso(estafeta(Id, Nome, Rating), estafeta(Id, Nome, RatingNovo)) :- RatingNovo is Rating+1.


estafetaEntregaFalhou(estafeta(Id, Nome, 0), estafeta(Id, Nome, 0)):- !.
estafetaEntregaFalhot(estafeta(Id, Nome, Rating), estafeta(Id, Nome, RatingNovo)) :- RatingNovo is Rating-1.
% Prazo não cumprido por parte do estafeta -> Diminuir o seu número de entregas

% 0 <= Rating <= 5


% 5. Definição preço de entrega
preco(encomenda(_, carro, _, _, _, _), P) :- P is Encomenda * TransporteUtilizado.
%entrega(2, carro, 1, rating, data(23,12,2), hora(18,40)).


% 6. Meios de transporte

%Deviamos escolher um limite de horas de trabalho por dia
%Porque ele não passa 24 horas na estrada
calculaVelocidade(Distancia, data(Dia, Mes, Ano), Velocidade) :-
    Horas is Dia*24+Mes*30*24+Ano*365*24,
    Velocidade is Horas/Distancia.

descobreCidade(Id, Cidade) :-
    rua(Id, Cidade, _).

distanciaPorRua(Rua, CidadeDest, Res) :-
    descobreCidade(Rua, CidadeOrigem),
    distancia(CidadeDest, CidadeOrigem, Res).

decideTransporte(_, encomenda(_, Peso, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, Peso, Data1, Data2, _, Rua), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distanciaPorRua(Rua, Cidade, Distancia),
    velocidadeEntrega is DataEntrega/Distancia,
    velocidadeEntrega < 10.
    

%Decide meio transporte
decideTransporte(_, encomenda(_, Peso, _, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, Peso, Data1, Data2, _, Rua, _), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distancia(Rua, Cidade, Distancia),
    velocidadeEntrega is DataEntrega/Distancia,
    velocidadeEntrega < 10.
    
% -> Vertente Ecológica dos meios de transporte pode ser descrita através de uma lista ordenada.
% Em que o primeiro elemento da lista pode ser, por exemplo, o mais ecológico e assim em diante...
ecologicos([bicicleta, moto, carro]).


%Funções auxiliares
pertencem([], _).
pertencem([L1|R1], Tudo):-
    membro(L1, Tudo),
    \+ membro(L1, R1),
    pertencem(R1, Tudo).

pertencem([L1|R1], Tudo):-
    \+ membro(L1, Tudo), !, false.

membro(X, [X|_]).
membro(X, [_|Xs]):-
        membro(X, Xs).


tamLista([], 0).
tamLista([X|R], N) :- 
    tamLista(R, TamNew),
    N is TamNew+1.

entregasNC([entrega(2, carro, 1, rating, data(23,12,2), hora(18,40)), entrega(2, carro, 1, rating, data(23,12,3000), hora(18,40)), entrega(2, carro, 1, rating, data(23,12,2019), hora(18,40)), entrega(3, bicicleta, 1, rating, data(23,12,2039),hora(18,40))]).
entregasC([entrega(2, carro, 1, rating, data(23,12,4), hora(18,40)),  entrega(2, carro, 1, rating, data(23,12,2019), hora(18,40)), entrega(3, bicicleta, 1, rating, data(23,12,2039),hora(18,40))]).
%Para testar:
% entregaEntreDatas(data(20, 12, 2019), data(25, 12, 2019), [entrega(2, carro, 1, rating, data(23,12,2019), hora(18,40)), entrega(3, bicicleta, 1, rating, data(23,12,2039),hora(18,40))], X).

%Encomendas - fora das duas datas = EncomendasFiltradas

entregaEntreDatas(D1, D2, Encomendas, EncomendasFiltradas) :- %findall(X, entregaEntreDatasFindAll(D1, D2, X)).
    %Todas as encomendas devem pertencer a EncomendasFiltradas
    %%pertencem(EncomendasFiltradas, Encomendas),
    entregaEntreDatasAux(D1, D2, Encomendas, Encomendas, EncomendasFiltradas).

%Versão que não recebe encomendas
entregaEntreDatas(D1, D2, EncomendasFiltradas) :- %findall(X, entregaEntreDatasFindAll(D1, D2, X)).
    entregaEntreDatasAux(D1, D2, EncomendasFiltradas).
%
%entrega(2, carro, 1, rating, data(23,12,4), hora(18,40)).
%entregaEntreDatas2(D1, D2, EncomendasFiltradas) :- 
%    findall(Entrega, entregaEntreDatasFindAll(D1, D2, Entrega), EncomendasFiltradas).

%
%entregaEntreDatasFindAll(D1, D2, entrega(_, _, _, _, Data, _)):- estaEntreDuasDatas(D1, D2, Data).

%Todas as encondas filtradas tem de estar nas Encomendas.
entregaEntreDatasAux(_, _, X, [], Filtrada) :- pertencem(Filtrada, X).
entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
    estaEntreDuasDatas(D1, D2, Data),
    entregaEntreDatasAux(D1, D2, X, L, Resto).

%Versão sem receber listas

entregaEntreDatasAux(_, _, []).
entregaEntreDatasAux(D1, D2, [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
    estaEntreDuasDatas(D1, D2, Data),
    entregaEntreDatasAux(D1, D2, Resto).


entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
    estaEntreDuasDatas(D1, D2, Data),
    entregaEntreDatasAux(D1, D2, X, L, Resto).

entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], Resto) :-
    \+ estaEntreDuasDatas(D1, D2, Data),
    entregaEntreDatasAux(D1, D2, X, L, Resto).



/* 
*  Conta o número de vezes que cada estafeta utilizou cada veículo retornando uma lista com esta ordem Bicicleta, Mota, Carro
*
*  1º: Lista de entregas do estafeta
*  2º: Número de vezes que utilizou bicicleta
*  3º: Número de vezes que utilizou moto
*  4º: Número de vezes que utilizou carro
*/
contaVeiculos([],0,0,0).
contaVeiculos([entrega(_,bicicleta,_,_,_)|T], NovoNBicla, NMoto, NCarro) :-
    contaVeiculos(T, NBicla, NMoto, NCarro),
    NovoNBicla is NBicla + 1
.
contaVeiculos([entrega(_,moto,_,_,_)|T], NBicla, NovoNMoto, NCarro) :-
    contaVeiculos(T, NBicla, NMoto, NCarro),
    NovoNMoto is NMoto + 1
.
contaVeiculos([entrega(_,carro,_,_,_)|T], NBicla, NMoto, NovoNCarro) :-
    contaVeiculos(T,NBicla,NMoto,NCarro),
    NovoNCarro is NCarro + 1
.

/*
*  Vê dos dois estafetas tem maior nº de usos e retorna o maior...
*
*  1º: (ID do estafeta)                                       /    (Nº de vezes que utilizou o veículo)
*  2º: (ID do outro estafeta)                                 /    (Nº de vezes que utilizou o veículo)
*  3º: (ID do estafeta que utilizou mais vezes o veículo)     /    (Nº de vezes que utilizou o veículo)
*/
veMaior(ID1/N1, ID2/N2, ID1/N1) :- N1 > N2.
veMaior(ID1/N1, ID2/N2, ID2/N2) :- N2 >= N1.

% Identifica que encomendas um cliente fez.
% encomendas_cliente: clienteID, encomendaID* -> {V, F}
encomendas_cliente(ClienteID, EncomendaID) :- 
  findall(EncID, entrega_cliente(EncID, ClienteID), EncomendaID).

% Identifica que cliente fez a encomenda
% entrega_cliente: EncomendaID, ClienteID -> {V,F}
entrega_cliente(EncID, ClienteID) :- 
  encomenda(EncID, ClienteID, _, _, _, _, _), entrega(_, _, EncID, _, _, _).

% Identifica que estafeta entregou a encomenda
% estafeta_entregou_encomenda: encomendaID, estafetaID -> {V,F}
estafeta_entregou_encomenda(EncID, EstID) :- entrega(EstID, _, EncID,  _, _).

/*
 *  Percorre uma lista de pares Rua/Counter e retorna o que tem o maior counter
 *
 *  Nota: Esta função não foi implementada está aqui caso queiramos que a função
 *        ruaMaisEntregue retorne apenas a rua mais entregue
 *  
 *  1º: Lista de pares Rua/Counter a ser percorrida
 *  2º: Resultado
 */
calculaMaior([], 0/0).
calculaMaior([Zona/NEnts|T], RZona/RNEnts) :-
    calculaMaior(T, TempZona/TempNEnts),
    veMaior(Zona/NEnts, TempZona/TempNEnts, RZona/RNEnts)
.

%Query 9    
filtraEncomendas(D1, D2, X):-
    encomenda(X, _, _, _, Data, _, _),
    estaEntreDuasDatas(D1, D2, Data).

quaisForamEntregues([], 0).
quaisForamEntregues([X|R], N) :- 
    entrega(_, _, X, _, _, _),
    quaisForamEntregues(R, TamNew),
    N is TamNew+1.
/*
 *  Adiciona N ao counter da rua ou adiciona o par Rua/N caso a rua não exista na lista
 *  
 *  1º: Par Rua/N que vai ser adicionado
 *  2º: Lista a que vai ser adicionado
 *  3º: Resultado
 */
addCounterCidade(Rua/N, [], [Rua/N]).
addCounterCidade(Rua/N, [Rua/N1|T], [Rua/N2|T]) :-
    N2 is N+N1
.
addCounterCidade(Rua/N, [OutraRua/N1|T], [OutraRua/N1|L]) :-
    OutraRua \= Rua,
    addCounterCidade(Rua/N, T, L)
.

/*
 *  Semelhante a addCounterCidade mas faz para uma lista de pares Rua/N
 *  
 *  1º: Lista de pares a adicionar
 *  2º: Lista a que vai ser adicionado
 *  3º: Resultado
 */
addCounterCidadeLista([],L,L).
addCounterCidadeLista([Rua/N|T], L, R) :-
    addCounterCidade(Rua/N,L,NovaL),
    addCounterCidadeLista(T, NovaL, R)
.

/*
 *  Percorre uma lista de entregas e retorna uma lista de pares Rua/Counter onde counter
 *  é o número de vezes que Rua apareceu na lista de entregas
 *
 *  1º: Lista de entregas
 *  2º: Resultado
 */
contaEntregasCidade([],[]).
contaEntregasCidade([entrega(_,_,IDEnc,_,_,_,_)|T], NovaL) :-
    contaEntregasCidade(T,L),
    encomenda(IDEnc,_,_,_,_,_, Rua),
    addCounterCidade(Rua/1, L, NovaL)
.

%Query 10
%Retorna as entregas feitas pelo Estafeta
entregasDoEstafeta(IdEstafeta, IdsEnTregasFeitas):-
  findall(X, selecionaIdsEncomendas(X, IdEstafeta), IdsEnTregasFeitas).
    
    
selecionaIdsEncomendas(X, IdEstafeta) :- 
  entrega(IdEstafeta, _, X, _, _, _).

%Recebe as entregas, procura as encomendas e soma pesos
%Está certa
calculaPesoPorEncomendas([], 0). 
calculaPesoPorEncomendas([ IdEncomenda|Resto], PesoTotal):- 
    encomenda(IdEncomenda, _, Peso, _, _, _, _),
    calculaPesoPorEncomendas(Resto, PesoNovo),
    PesoTotal is PesoNovo + Peso.