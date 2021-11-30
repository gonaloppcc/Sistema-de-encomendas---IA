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
preco(entrega(A, bicicleta, EncID, B, Data2, C), P) :- precoEntregaAux(entrega(A, bicicleta, EncID, B, Data2, C), Coef),
            P is 5 * Coef.

preco(entrega(A, mota, EncID, B, Data2, C), P) :- precoEntregaAux(entrega(A, bicicleta, EncID, B, Data2, C), Coef),
            P is 10 * Coef.

preco(entrega(A, carro, EncID, B, Data2, C), P) :- precoEntregaAux(entrega(A, bicicleta, EncID, B, Data2, C), Coef),
            P is 20 * Coef.
%encomenda(1, 1, 20, 25, data(1,1,1), data(4,5,1), 2).
%encomenda: encomendaID, clienteID, peso, volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, ruaID -> {V,F}. 

% Calcula o coeficiente de entrega dado os seus atributos como o Peso, Vol e o tempo passado desde que foi encomendada.
precoEntregaAux(entrega(_, _, EncID, _, Data2, _), Coef) :- encomenda(EncID, _, Peso, Vol, _, _, Data1, _, _),
            intervaloTempo(Data1, Data2, data(D, M, A)),
            PastTime is D + M + A,
            write(PastTime + ' '),
            Coef is Peso * Vol / PastTime.


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
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, _, _, _, Data1, _, Data2, _, Rua), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distanciaPorRua(Rua, Cidade, Distancia),
    VelocidadeEntrega is DataEntrega/Distancia,
    VelocidadeEntrega < 10.
    

%Decide meio transporte
decideTransporte(_, encomenda(_, Peso, _, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, _, _, _, Data1, _, Data2, _, Rua), transporte(bicicleta, 5, 10)) :-
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
tamLista([_|R], N) :- 
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
veMaior(ID1/N1, _/N2, ID1/N1) :- N1 > N2.
veMaior(_/N1, _/N2, _/N2) :- N2 >= N1.

% Identifica que encomendas um cliente fez.
% encomendas_cliente: clienteID, encomendaID* -> {V, F}
encomendas_cliente(ClienteID, EncomendaID) :- 
  findall(EncID, entrega_cliente(EncID, ClienteID), EncomendaID).

% Identifica que cliente fez a encomenda
% entrega_cliente: EncomendaID, ClienteID -> {V,F}
entrega_cliente(EncID, ClienteID) :- 
  encomenda(EncID, ClienteID, _, _, _, _, _, _, _), entrega(_, _, EncID, _, _, _).

% Identifica que estafeta entregou a encomenda
% estafeta_entregou_encomenda: encomendaID, estafetaID -> {V,F}
estafeta_entregou_encomenda(EncID, EstID) :- entrega(EstID, _, EncID,  _, _, _).

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
%query 7

filtraEntregas(D1, D2, Veiculo):-
    entrega(_, Veiculo, _, _, Data, _),
    estaEntreDuasDatas(D1, D2, Data).
%Query 8

%entrega: estafetaID, veiculo, encomendaID, rating, dataEntrega, Hora -> {V,F}
entregaEntreDatas(D1, D2, IdEstafeta) :- 
    entrega(IdEstafeta, _, _, _, Data, _),
    estaEntreDuasDatas(D1, D2, Data).

contaPares([], []). 
contaPares([IdEst|Resto], RespostaPares) :-
    contaEelimina([IdEst|Resto], (IdEst, NEntregas), ListaLimpa),
    contaPares(ListaLimpa, Juntas),
    %write("OOO"),
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
    encomenda(X, _, _, _, Data, _, _, _, _),
    estaEntreDuasDatas(D1, D2, Data).

%O findall vai dar os estafetas
quaisForamEntregues([],0, 0). 
quaisForamEntregues([X|R], N, NNentregues) :- 
    findall(XX, entrega(XX, _, X, _, _, _), ListaEncomendas),
    tamLista(ListaEncomendas, Bool),
    Bool >= 1,
    quaisForamEntregues(R, TamNew, NNentregues),
    N is TamNew+1.

quaisForamEntregues([X|R], N, NNentregues) :- 
    findall(XX, entrega(XX, _, X, _, _, _), ListaEncomendas),
    tamLista(ListaEncomendas, 0),
    quaisForamEntregues(R, N, NNnovo),
    NNentregues is NNnovo+1.

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
    encomenda(X,_,_,_,_,_,_,_,Rua),
    encontraEncomendas(T,T1)
.

/*  Soma todos os elementos de uma lista
 * 
 *  1º: Lista a somar
 *  2º: Soma de todos os elementos
 */
sum([],0).
sum([X|T],N) :-
    sum(T,N1),
    N is N1+X
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
    encomenda(IdEncomenda, _, Peso, _, _, _, _, _, _),
    calculaPesoPorEncomendas(Resto, PesoNovo),
    PesoTotal is PesoNovo + Peso.
