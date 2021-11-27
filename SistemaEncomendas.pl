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
preco(entrega(_, bicicleta, _, _, _, _), P) :- P is 5.
preco(entrega(_, mota, _, _, _, _), P) :- P is 10.
preco(entrega(_, carro, _, _, _, _), P) :- P is 20.
%encomenda(1, 1, 20, 25, data(1,1,1), data(4,5,1), 2).



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
    VelocidadeEntrega is DataEntrega/Distancia,
    VelocidadeEntrega < 10.
    

%Decide meio transporte
decideTransporte(_, encomenda(_, Peso, _, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, Peso, Data1, Data2, _, Rua, _), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distancia(Rua, Cidade, Distancia),
    VelocidadeEntrega is DataEntrega/Distancia,
    VelocidadeEntrega < 10.
    
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




/* Verifica o estafeta que usou mais vezes cada veiculo 
*
*  1º: Lista de triplos Estafeta/Veiculo/N onde N é o número de vezes que usou o veiculo
*  2º: Estafeta que utilizou mais a bicicleta/N
*  3º: Estafeta que utilizou mais a moto/N
*  4º: Estafeta que utilizou mais o carro/N
*/
contaVeiculos([],0/0,0/0,0/0).
contaVeiculos([ID/bicicleta/N|T],RID1/RN1,ID2/N2,ID3/N3) :-
    contaVeiculos(T,ID1/N1,ID2/N2,ID3/N3),
    veMaior(ID/N,ID1/N1,RID1/RN1)
.
contaVeiculos([ID/moto/N|T],ID1/N1,RID2/RN2,ID3/N3) :-
    contaVeiculos(T,ID1/N1,ID2/N2,ID3/N3),
    veMaior(ID/N,ID2/N2,RID2/RN2)
.
contaVeiculos([ID/carro/N|T],ID1/N1,ID2/N2,RID3/RN3) :-
    contaVeiculos(T,ID1/N1,ID2/N2,ID3/N3),
    veMaior(ID/N,ID3/N3,RID3/RN3)
.

/* Vê dos dois estafetas tem maior nº de usos e retorna o maior...
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
%Query 8
%Encomendas - fora das duas datas = EncomendasFiltradas

%entregaEntreDatas(D1, D2, Encomendas, EncomendasFiltradas) :- %findall(X, entregaEntreDatasFindAll(D1, D2, X)).
%    %Todas as encomendas devem pertencer a EncomendasFiltradas
%    %%pertencem(EncomendasFiltradas, Encomendas),
%    entregaEntreDatasAux(D1, D2, Encomendas, Encomendas, EncomendasFiltradas).
%
%%Versão que não recebe encomendas
%entregaEntreDatas(D1, D2, EncomendasFiltradas) :- %findall(X, entregaEntreDatasFindAll(D1, D2, X)).
%    entregaEntreDatasAux(D1, D2, EncomendasFiltradas).
%%
%%entrega(2, carro, 1, rating, data(23,12,4), hora(18,40)).
%%entregaEntreDatas2(D1, D2, EncomendasFiltradas) :- 
%%    findall(Entrega, entregaEntreDatasFindAll(D1, D2, Entrega), EncomendasFiltradas).
%
%%
%%entregaEntreDatasFindAll(D1, D2, entrega(_, _, _, _, Data, _)):- estaEntreDuasDatas(D1, D2, Data).
%
%%Todas as encondas filtradas tem de estar nas Encomendas.
%entregaEntreDatasAux(_, _, X, [], Filtrada) :- pertencem(Filtrada, X).
%entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
%    estaEntreDuasDatas(D1, D2, Data),
%    entregaEntreDatasAux(D1, D2, X, L, Resto).
%
%%Versão sem receber listas
%
%entregaEntreDatasAux(_, _, []).
%entregaEntreDatasAux(D1, D2, [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
%    estaEntreDuasDatas(D1, D2, Data),
%    entregaEntreDatasAux(D1, D2, Resto).
%
%
%entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], [entrega(X1, X2, X3, X4, Data, X5)|Resto]) :-
%    estaEntreDuasDatas(D1, D2, Data),
%    entregaEntreDatasAux(D1, D2, X, L, Resto).
%
%entregaEntreDatasAux(D1, D2, X, [entrega(X1, X2, X3, X4, Data, X5)|L], Resto) :-
%    \+ estaEntreDuasDatas(D1, D2, Data),
%    entregaEntreDatasAux(D1, D2, X, L, Resto).


%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
entregaEntreDatas(D1, D2, IdEstafeta) :- 
    entrega(IdEstafeta, _, _, _, Data, _),
    estaEntreDuasDatas(D1, D2, Data).

contaPares([], _). 
contaPares([IdEst|Resto], RespostaPares) :-
    contaEelimina([IdEst|Resto], (IdEst, NEntregas), ListaLimpa),
    contaPares(ListaLimpa, Juntas),
    adic((IdEst, NEntregas), RespostaPares, Juntas)
    .
contaEelimina([], (1000, 0), []).
contaEelimina(Lista, (IdEst, NEntregas), ListaLimpa) :-
    count(IdEst, Lista, NEntregas),
    apagaT(IdEst, Lista, ListaLimpa).

%Funções sobre listas
%Conta quandos elementos tem essa lista
count(_, [], 0).
count(X, [X | T], N) :-
  !, count(X, T, N1),
  N is N1 + 1.
count(X, [_ | T], N) :-
  count(X, T, N).

%Apaga os elementos iguais a X nessa lista
apagaT(_, [], []).
apagaT(X, [X|T], L) :- apagaT(X, T, L).
apagaT(X, [H|T], [H|T1]) :- X \= H, apagaT(X, T, T1).

%Adiciona um elemento à lista
adic(X, [], [X]):- !.
adic(X, L1, [X|L1]).

%Query 9    
filtraEncomendas(D1, D2, X):-
    encomenda(X, _, _, _, Data, _, _),
    estaEntreDuasDatas(D1, D2, Data).

quaisForamEntregues([],0). 
quaisForamEntregues([X|R], N) :- 
    findall(XX, entrega(_, _, X, _, _, _), ListaEncomendas),
    tamLista(ListaEncomendas, Bool),
    Bool >= 1,
    quaisForamEntregues(R, TamNew),
    N is TamNew+1.
quaisForamEntregues([X|R], N) :- 
    findall(XX, entrega(_, _, X, _, _, _), ListaEncomendas),
    tamLista(ListaEncomendas, 0),
    quaisForamEntregues(R, N).

auxQ9([], 0).
auxQ9([H|T], H).
/*  Sememlhante ao maplist mas a segunda lista é passada na sua totalidade para todos os elementos da primeira lista
 *  
 *  1º: Função a executar
 *  2º: Lista com os vários elementos que serão passados à função
 *  3º: Lista que será passada na sua totalidade para todos os elementos da primeira lista
 *  4º: Resultado de todas as execuções da função
 */
aplicaLista(_,[],_,[]).
aplicaLista(Func,[X|T],L,[R|T2]) :-
    call(Func,X,L,R),
    aplicaLista(Func,T,L,T2)
.

/*  Encontra todos os elementos únicos de uma lista
 * 
 *  1º: Lista a filtrar
 *  2º: Lista filtrada
 */
encontraUnicos([],[]).
encontraUnicos([X|T],[X|L]) :-
    encontraUnicos(T,L),
    \+ member(X,L)
.
encontraUnicos([X|T],L) :-
    encontraUnicos(T,L),
    member(X,L)
.

/*  Conta quantas vezes o elemento aparece na lista
 *
 *  1º: Elemento a contar
 *  2º: Lista a procurar
 *  3º: Par Elem/N onde N é o número de vezes que elemento aparece na lista
 */
contaElem(Elem,[],Elem/0).
contaElem(Elem,[Elem|T],Elem/N) :-
    contaElem(Elem,T,Elem/N1),
    N is N1 + 1
.
contaElem(Elem,[X|T],Elem/N) :-
    Elem \= X,
    contaElem(Elem,T,Elem/N)
.

/*  Encontra as encomendas relacionadas com as entregas de uma lista
 *
 *  1º: Lista a de entregas
 *  2º: Lista de encomendas
 */
encontraEncomendas([],[]).
encontraEncomendas([X|T],[Rua|T1]) :-
    encomenda(X,_,_,_,_,_,Rua),
    encontraEncomendas(T,T1)
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
