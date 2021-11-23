
:- include('baseConhecimento.pl').

% Falta resumir os objetivos/queries aqui
%
% Query 1
% Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
estafetaMaisEcologico(Estafeta) :- findAll(estafeta, include(estafeta)).



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
