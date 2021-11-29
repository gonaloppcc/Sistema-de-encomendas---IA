% Objetivo: Entregar todas as encomendas que ainda foram entregues.

% Entrega todas as encomendas que não tenham sido entregues
entregaEncomendas(Encs) :- 
    findall(encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), 
    (encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), \+ entrega(_, _, Id, _, _, _)),
    Encs), % Todas as encomendas não entregues.
    foldl(entregaEncomenda, Encs, true, V).

entregaEncomenda(encomenda(EncomendaID, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua)) :-
    random(0, 20, EstafetaID),
    Veiculo = carro,
    random(0, 5, Rating),
    DataEntrega = data(27, 11, 2021),
    HoraEntrega = hora(23, 40),
    %evolucao(entrega(EstafetaID, carro, EncomendaID, Rating, DataEntrega, HoraEntrega)).
    assert(entrega(EstafetaID, carro, EncomendaID, Rating, DataEntrega, HoraEntrega)).
