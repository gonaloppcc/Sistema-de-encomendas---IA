
:- include('baseConhecimento.pl').
:- include('SistemaEncomendas.pl').

/* TODO: Falta resumir os objetivos/queries aqui
*
*  Query 1
*  Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
*/

/* 
*  Retorna o estafeta que utilizou mais vezes cada um dos meios de transporte junto com o número de vezes que o utilizou
*
*  1º: Lista de pares estafeta/entregas
*  2º: ID do estafeta que utilizou mais vezes a bicicleta    /    nº de vezes que a utilizou
*  3º: ID do estafeta que utilizou mais vezes a moto         /    nº de vezes que a utilizou
*  4º: ID do estafeta que utilizou mais vezes o carro        /    nº de vezes que o utilizou
*/
estafetaMaisEco([], 0/0, 0/0, 0/0).
estafetaMaisEco([ID/Entregas|T], RID1/RNBicla, RID2/RNMoto, RID3/RNCarro) :-
    estafetaMaisEco(T, ID1/NBicla, ID2/NMoto, ID3/NCarro),
    contaVeiculos(Entregas, NovoNBicla, NovoNMoto, NovoNCarro),
    veMaior(ID/NovoNBicla, ID1/NBicla, RID1/RNBicla),
    veMaior(ID/NovoNMoto, ID2/NMoto, RID2/RNMoto),
    veMaior(ID/NovoNCarro, ID3/NCarro, RID3/RNCarro)
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
estafeta_clientes(ID, [ID/entregas|T], Clientes) :-
    clientes_entregues(entregas, Clientes)
.
estafeta_clientes(ID, [ID2/entregas|T], Clientes) :-
    ID \= ID2,
    estafeta_clientes(ID,T,Clientes).


/*
 *  Query 5
 *
 *  Retorna uma lista com todos os pares ruas/(vezes que foi entregue)
 *
 *  1º: Lista com pares estafeta/entregas
 *  2º: Resultado
 *
 * TODO: Corrigir o facto de ao precionar ";" a função continua a vomitar valores
 *       apesar de serem sempre iguais.
 */
ruaMaisEntregue([], []).
ruaMaisEntregue([_/Entregas|T], NovaL) :-
    ruaMaisEntregue(T, L),
    contaEntregasCidade(Entregas, Contadas),
    addCounterCidadeLista(Contadas,L, NovaL)
.