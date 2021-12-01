
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
estafetaMaisEco(ID1/N1,ID2/N2,ID3/N3) :-
    findall(Estafeta/Veiculo, entrega(Estafeta,Veiculo,_,_,_,_), Entregas),
    encontraUnicos(Entregas,Filtrados),
    aplicaLista(contaElem,Filtrados,Entregas,Contados),
    contaVeiculos(Contados,ID1/N1,ID2/N2,ID3/N3)
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
    findall(Rating, entrega(Estafeta,_,EncID,Rating,_,_), Ratings),
    sum(Ratings,Sum),
    length(Ratings, NRatings),
    NRatings > 0, N is Sum/NRatings, !
.
satisfacClienteParaEstafeta(_,0).

%Query 7

entregasPorMeioTransporte(Data1, Data2, ListaRes) :-
    findall(X, filtraEntregas(Data1, Data2, X), ListaVeiculos),
    contaPares(ListaVeiculos, ListaRes).

%Query 8

numeroEncomendas(Data1, Data2, RespostaPares) :-
    findall(IdEstafeta, entregaEntreDatas(Data1, Data2, IdEstafeta), Pares),
    contaPares(Pares, RespostaPares).
    %tamLista(EncomendasFiltradas, NTotal).

%Query 9 Filtra pelo prazo
encomendasNEntregues(D1, D2, NToal, NTotalNEntregues) :-
    findall(X, filtraEncomendas(D1, D2, X), ListaEncomendas),
    quaisForamEntregues(ListaEncomendas, NToal, NTotalNEntregues).


%Query 10
%Mas ele duplica uma entrega do estafeta 2, não sei se o problema é da baseConhecimento, mas não parece.
%Mas está na entregasDoEstafeta
totalPesoEstafeta(IdEstafeta, PesoTotal) :-
  entregasDoEstafeta(IdEstafeta, IdsEnTregasFeitas),
  calculaPesoPorEncomendas(IdsEnTregasFeitas, PesoTotal).
