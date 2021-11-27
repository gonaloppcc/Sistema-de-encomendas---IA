
:- include('baseConhecimento.pl').
:- include('SistemaEncomendas.pl').

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

%
% encomendas_cliente: clienteID, encomendaID* -> {V, F}
encomendas_cliente(ClienteID, EncomendaID) :- 
  findall(EncID, entrega_cliente(EncID, ClienteID), EncomendaID).

% entrega_cliente: EncomendaID, ClienteID -> {V,F}
entrega_cliente(EncID, ClienteID) :- 
  encomenda(EncID, ClienteID, _, _, _, _, _), entrega(_, _, EncID, _, _).

% 
% estafeta_entregou_encomenda: encomendaID, estafetaID -> {V,F}
estafeta_entregou_encomenda(EncID, EstID) :- entrega(EstID, _, EncID,  _, _).



% Query 3
/*  Retorna uma lista de clientes servidos pelo estafeta dado
 *
 *  1º: Estafeta a procurar
 *  2º: Lista de clientes servidos pelo estafeta
 */
clientesServidos(Estafeta,Clientes) :-
    findall(Cliente, (entrega(Estafeta,_,EncID,_,_,_),encomenda(EncID,Cliente,_,_,_,_,_)), Clientes1),
    encontraUnicos(Clientes1, Clientes)
.


% Query 4
%  Calcular o valor faturado pela Green Distribution num determinado dia;
valorFaturado(data(Dia, Mes, Ano), Encomendas) :-
    findall(entrega(A, B, C, D, data(Dia, Mes, Ano), E), entrega(A, B, C, D, data(Dia, Mes, Ano), E), Encomendas).
    %maplist(preco, Encomendas, Precos).
    %foldl(plus, Precos, 0, Valor).



/*
 *  Query 5
 *
 *  Percorre uma lista de entregas e retorna uma lista de pares Rua/Counter onde counter
 *  é o número de vezes que Rua apareceu na lista de entregas
 *
 *  1º: Lista de entregas
 *  2º: Resultado
 */
/* TODO: Pôr esta versão direito e apagar a outra
entregasEmCadaRua(R) :-
    findall(Rua, (entrega(_,_,EncID,_,_,_),encomenda(EncID,_,_,_,_,_,Rua)), Ruas),
    encontraUnicos(Ruas,Filtrados),
    aplicaLista(contaElem,Filtrados,Ruas,R)
.
*/
entregasEmCadaRua(R) :-
    findall(EncID, entrega(_,_,EncID,_,_,_),IDs),
    encontraEncomendas(IDs,Ruas),
    encontraUnicos(Ruas,Filtrados),
    aplicaLista(contaElem,Filtrados,Ruas,R),
    !
.

%Query 8
numeroEncomendas(Data1, Data2, Encomendas, NTotal) :-
    entregaEntreDatas(Data1, Data2, Encomendas, EncomendasFiltradas),
    tamLista(EncomendasFiltradas, NTotal).

%Versão sem Lista
%Falta testar, não está a dar bem não sei porquê, é no *estaEntreDuasDatas*
numeroEncomendas(Data1, Data2, RespostaPares) :-
    findall(IdEstafeta, entregaEntreDatas(D1, D2, IdEstafeta), Pares),
    contaPares(Pares, RespostaPares).
    %tamLista(EncomendasFiltradas, NTotal).

%Query 9 Filtra pelo prazo
encomendasNEntregues(D1, D2, NToal) :-
    findall(X, filtraEncomendas(D1, D2, X), ListaEncomendas),
    quaisForamEntregues(ListaEncomendas, NToal).


%Query 10
%Mas ele duplica uma entrega do estafeta 2, não sei se o problema é da baseConhecimento, mas não parece.
%Mas está na entregasDoEstafeta
totalPesoEstafeta(IdEstafeta, PesoTotal) :-
  entregasDoEstafeta(IdEstafeta, IdsEnTregasFeitas),
  calculaPesoPorEncomendas(IdsEnTregasFeitas, PesoTotal).
