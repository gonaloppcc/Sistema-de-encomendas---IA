
:- include('baseConhecimento.pl').

% Falta resumir os objetivos/queries aqui
%
% Query 1
% Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
estafetaMaisEcologico(Estafeta) :- findAll(estafeta, include(estafeta)).

% Conta o número de vezes que cada estafeta utilizou cada veículo retornando uma lista com esta ordem [Bicicleta,Mota,Carro]
contaVeiculos([], NumBicla, NumMota, NumCarro, [NumBicla,NumMota,NumCarro]).
contaVeiculos([entrega(_,bicicleta,_,_,_)|T],NumBicla,NumMota,NumCarro, R) :-
    NovoNumBicla is NumBicla + 1,
    contaVeiculos(T,NovoNumBicla,NumMota,NumCarro, R)
.
contaVeiculos([entrega(_,mota,_,_,_)|T],NumBicla,NumMota,NumCarro, R) :-
    NovoNumMota is NumMota + 1,
    contaVeiculos(T,NumBicla,NovoNumMota,NumCarro, R)
.
contaVeiculos([entrega(_,carro,_,_,_)|T],NumBicla,NumMota,NumCarro, R) :-
    NovoNumCarro is NumCarro + 1,
    contaVeiculos(T,NumBicla,NumMota,NovoNumCarro, R)
.

% Igual ao contaVeículo só que é para um específico. 
% Eu queria mandar isto co caralho e usar a contaVeículo mas ainda não vi uma maneira de a implementar e tou com sono
% TODO: Mandar esta merda co caralho.
contaBicla([],0).
contaBicla([entrega(_,bicicleta,_,_,_)|T],NovoNBicla) :-
    contaBicla(T,NBicla),
    NovoNBicla is NBicla + 1
.
contaBicla([entrega(_,_,_,_,_)|T],NBicla) :-
    contaBicla(T,NBicla)
.
contaMoto([],0).
contaMoto([entrega(_,moto,_,_,_)|T],NovoNMoto) :-
    contaMoto(T,NMoto),
    NovoNMoto is NMoto + 1
.
contaMoto([entrega(_,_,_,_,_)|T],NMoto) :-
    contaMoto(T,NMoto)
.
contaCarro([],0).
contaCarro([entrega(_,carro,_,_,_)|T],NovoNCarro) :-
    contaCarro(T,NCarro),
    NovoNCarro is NCarro + 1
.
contaCarro([entrega(_,_,_,_,_)|T],NCarro) :-
    contaCarro(T,NCarro)
.

% Retorna uma lista com o estafeta que utilizou mais vezes cada um dos meios de transporte junto com o número de vezes que o utilizou
% TODO: Simplificar esta merda
estafetaMaisEco([], ID1/NBicla, ID2/NMota, ID3/NCarro, [ID1/NBicla,ID2/NMota,ID3/NCarro]).
estafetaMaisEco([ID/Entregas|T], ID1/NBicla, ID2/NMoto, ID3/NCarro, R) :-
    contaBicla(Entregas,NovoNBicla),
    contaMoto(Entregas,NovoNMoto),
    contaCarro(Entregas,NovoNCarro),
    NovoNBicla1 is max(NovoNBicla,NBicla),
    NovoNMoto1 is max(NovoNMoto,NMoto),
    NovoNCarro1 is max(NovoNCarro,NCarro),
    (NovoNBicla1 = NovoNBicla -> NID1 is ID; NID1 is ID1),
    (NovoNMoto1 = NovoNMoto -> NID2 is ID; NID2 is ID2),
    (NovoNCarro1 = NovoNCarro -> NID3 is ID; NID3 is ID3),
    estafetaMaisEco(T, NID1/NovoNBicla1, NID2/NovoNMoto1, NID3/NovoNCarro1, R)
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


%Query 8
numeroEncomendas(Data1, Data2, Encomendas, NTotal) :-
    entregaEntreDatas(Data1, Data2, Encomendas, EncomendasFiltradas),
    tamLista(EncomendasFiltradas, NTotal).

%Versão sem Lista
numeroEncomendas(Data1, Data2, NTotal) :-
    findall(Entrega, estaEntreDuasDatas((D1, D2), Entrega), EncomendasFiltradas),
    tamLista(EncomendasFiltradas, NTotal).
