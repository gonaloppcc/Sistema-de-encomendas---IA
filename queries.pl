
:- include('SistemaEncomendas.pl').
:- include('entregaEncomendas.pl').

:- dynamic encomenda/9.
:- dynamic entrega/6.

/* TODO: Falta resumir os objetivos/queries aqui
*
*  Query 1
*  Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
*/

/*  Retorna o estafeta que utilizou mais vezes cada um dos meios de transporte junto com o número de vezes que o utilizou
 *
 *  1º: ID do estafeta que utilizou mais vezes a bicicleta    /    nº de vezes que a utilizou
 *  2º: ID do estafeta que utilizou mais vezes a moto         /    nº de vezes que a utilizou
 *  3º: ID do estafeta que utilizou mais vezes o carro        /    nº de vezes que o utilizou
 */
estafetaMaisEco(R) :-
    findall(Estafeta/Veiculo, entrega(Estafeta,Veiculo,_,_,_,_), Entregas),
    encontraUnicos(Entregas,Filtrados),
    aplicaLista(contaElem,Filtrados,Entregas,Contados),
    contaVeiculos(Contados,R)
.

% Query 2
% Identificar que estafetas entregaram determinada(s) encomenda(s) a um determinado cliente;
% estafetas_clientes: estafetasID*, encomendasID*, clienteID -> {V,F}
estafetas_clientes(EstafetasID, EncomendasID, ClienteID) :-
  encomendas_cliente(ClienteID, EncomendasID),
  EncID = EncomendasID,
  maplist(estafeta_entregou_encomenda, EncID, EstafetasID).



% Query 3
/*  Retorna uma lista de clientes servidos pelo estafeta dado
 *
 *  1º: Estafeta a procurar
 *  2º: Lista de clientes servidos pelo estafeta
 */
clientesServidos(Estafeta,Clientes) :-
    findall(Cliente, (entrega(Estafeta,_,EncID,_,_,_),encomenda(EncID,Cliente,_,_,_,_,_,_,_)), Clientes1),
    encontraUnicos(Clientes1, Clientes)
.
%Query 4
/*
Calcular o valor faturado pela Green Distribution num determinado dia.
*/
lucroUmDia(dia(D1, M1, A1), Valor) :-
  findall(Encomenda, entrega(_, _, Encomenda, _, data(D1, M1, A1), _), ListaEncomendas),
  calculaLucroPorEncomendas(ListaEncomendas, Valor).



% Query 4
%  Calcular o valor faturado pela Green Distribution num determinado dia;
valorFaturado(data(Dia, Mes, Ano), Valor) :-
    findall(entrega(A, B, C, D, data(Dia, Mes, Ano), E), entrega(A, B, C, D, data(Dia, Mes, Ano), E), Encomendas),
    maplist(preco, Encomendas, Precos),
    foldl(plusFloat, Precos, 0, Valor).

plusFloat(N1, N2, N) :- N is N1 + N2.

/*
 *  Query 5
 *
 *  Percorre uma lista de entregas e retorna uma lista de pares Rua/Counter onde counter
 *  é o número de vezes que Rua apareceu na lista de entregas
 *
 *  1º: Lista de entregas
 *  2º: Resultado
 */
entregasEmCadaRua(R) :-
    findall(Rua, (entrega(_,_,EncID,_,_,_),encomenda(EncID,_,_,_,_,_,_,_,Rua)), Ruas),
    encontraUnicos(Ruas,Filtrados),
    aplicaLista(contaElem,Filtrados,Ruas,R)
. 

% Query 6
/*  Calcula a média de rating de todas as entregas de um determinado estafeta
 *  
 *  1º: Estafeta a procurar
 *  2º: Média de ratings
 */
satisfacClienteParaEstafeta(Estafeta,N) :-
    findall(Rating, entrega(Estafeta,_,_,Rating,_,_), Ratings),
    sum(Ratings,Sum),
    length(Ratings, NRatings),
    NRatings > 0, N is Sum/NRatings, !
.
satisfacClienteParaEstafeta(_,0).

%Query 7
/*
Identifica o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.
O findall procura as entregas entre as duas datas, e guarda o veículo utilizado.
O predicado contaPares conta os elementos da lista num par. 
Nesse par, o primeiro elemento é o elemento contado, e o segundo é o número de vezes que aparece.
*/
entregasPorMeioTransporte(Data1, Data2, ListaRes) :-
    findall(X, filtraEntregas(Data1, Data2, X), ListaVeiculos),
    contaPares(ListaVeiculos, ListaRes).

%Query 8
/*
Identifica  o  número  total  de  entregas  pelos  estafetas,  num  determinado intervalo de tempo.
O findall procura as entregas entre as duas datas, e guarda o ID do estafeta.
O predicado contaPares está descrito na query anterior.
*/
numeroEncomendas(Data1, Data2, RespostaPares) :-
    findall(IdEstafeta, entregaEntreDatas(Data1, Data2, IdEstafeta), Pares),
    contaPares(Pares, RespostaPares).

%Query 9 
/*
Calcula o número de encomendas entregues e não entregues pela Green Distribution, num determinado período de tempo.
O findall procura as entregas entre as duas datas, e guarda o ID da encomenda.
O predicado "quaisForamEntregues" verifica quais dessas encomendas foram ou não entregues. 
O predicado retorna em NTotal o número de encomendas entregues, e em NTotalNEntregues as não entregues.
*/
encomendasNEntregues(D1, D2, NTotal, NTotalNEntregues) :-
    findall(X, filtraEncomendas(D1, D2, X), ListaEncomendas),
    quaisForamEntregues(ListaEncomendas, NTotal, NTotalNEntregues).


%Query 10
/*
Calcula o peso total transportado por estafeta num determinado dia. 
O predicado "entregasDoEstafeta" procura quais as entregas feitas por um estafeta, num dia, guardando os ids das entregas.
O predicado "calculaPesoPorEncomendas" calcula o peso total dessas encomendas.
*/
totalPesoEstafeta(IdEstafeta, Data, PesoTotal) :-
  entregasDoEstafeta(IdEstafeta, Data, IdsEnTregasFeitas),
  calculaPesoPorEncomendas(IdsEnTregasFeitas, PesoTotal).
