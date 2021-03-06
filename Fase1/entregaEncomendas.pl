% Objetivo: Entregar todas as encomendas que ainda foram entregues.

% Entrega todas as encomendas que não tenham sido entregues
entregaEncomendas(Entregas) :- 
    findall(encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), 
    (encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), \+ entrega(_, _, Id, _, _, _)),
    Encs), % Todas as encomendas não entregues.
    maplist(entregaEncomenda, Encs, Entregas).

entregaEncomenda(encomenda(EncomendaID, _ , _, _, PrazoEntrega, HorasPrazoEntrega, _, _, _), Entrega) :-
    atribuido(EstafetaId, EncomendaID),
    Veiculo = carro,
    random(0, 5, Rating),
    DataEntrega = PrazoEntrega,
    HoraEntrega = HorasPrazoEntrega,
    Entrega = entrega(EstafetaId, carro, EncomendaID, Rating, DataEntrega, HoraEntrega),
    evolucao(Entrega).

/**
Diz quais os estafetas que podem entregar uma encomenda a partir do ID. 
Se a encomenda sair da Póvoa de Varzim, retorna os estafetas sediados nessa cidade.
*/
filtraCidadeEncomenda(EncomendaID, ListaEstafetas) :-
    encomenda(EncomendaID, _, _, _, _, _, _, _, RuaId),
    rua(RuaId, City, _),
    findall(X, estafeta(X, _, City), ListaEstafetas). 

/*
Verifica se um dado estafeta está livre nesse dia em função do peso máximo que pode transportar nesse dia.
Atualmente o peso máximo é 100, que pode levar num carro.
O predicado procura todas as encomendas de um estafeta, filtra pelo dia, e calcula a soma dos pesos das encomendas.
*/
estafetaLivre(EstafetaId, Data) :-
    findall(IdsEncomendas, atribuido(EstafetaId, IdsEncomendas), ListaEncomendas),
    verificaListaEncomendasQuantasNumDia(ListaEncomendas, Data, PesoNumDia),
    PesoNumDia =< 100.


getDataFromEncomenda(EncomendaId, DataDessaEncomenda) :- encomenda(EncomendaId, _, _, _, DataDessaEncomenda, _, _, _, _ ).
/*
Diz quantas encomendas estão planeadas para ser entregues num dado dia - data(dia, mes, ano).
A linha do maplist converte Id's de encomendas em datas.
O include filtra as encomendas pela data dada.
*/
verificaListaEncomendasQuantasNumDia(Lista, Data, PesoNumDia) :-
    fazParesDataPeso_DeIdsEncomendas(Lista, ListaPares),
    %maplist(getDataFromEncomenda, Lista, Datas),
    include(comparaDatas(Data), ListaPares, DatasIguaisADada ),
%Mas o critério é o peso total das encomendas desse dia
    sumPair(DatasIguaisADada, PesoNumDia).

fazParesDataPeso_DeIdsEncomendas([], []).
fazParesDataPeso_DeIdsEncomendas([IdEncomenda|Resto], Pares) :-
    encomenda(IdEncomenda, _, Peso, _, Data, _, _, _, _),
    adic((Data, Peso), ResRecursivo, Pares),
    fazParesDataPeso_DeIdsEncomendas(Resto, ResRecursivo).

sumPair([], 0).
sumPair([(_, Peso)|T], Res) :- 
    sumPair(T, ResNew),
    Res is ResNew+Peso.

/*
Gera atribuições a encomendas que não as tenham.
Processo:
Cria uma lista de ID's de encomendas que não tenham atribuições.
Para cada ID de uma encomenda, procura quais os estafetas que a podem entregar.
Verifica se o primeiro estafeta pode entregar. Pára no último estafeta.
Se for o último estafeta, pára e atribui-lhe.
Se sim, gera atribuição com esse par.
Se não, procura no elemento seguinte.
*/

gerarAtribuicoes() :-
    listaEncomendasNAtribuida(Lista),
    gerarAtribuicoesLista(Lista).

listaEncomendasNAtribuida(Res) :-
    findall(EncId, encomenda(EncId, _, _, _, _, _, _, _, _), ListaIDs ),
    findall(EncE, atribuido(_, EncE), ListaAtribuidas ),
    removeOneList(ListaIDs, ListaAtribuidas, Res).

gerarAtribuicoesLista([]).
gerarAtribuicoesLista([EncID|T]) :- geraUmaAtribuicao(EncID), gerarAtribuicoesLista(T).

geraUmaAtribuicao(EncId) :-
    filtraCidadeEncomenda(EncId, ListaEstafetas),
    getDataFromEncomenda(EncId, Data),
    procuraEstafetaLivreEnc(EncId, Data, ListaEstafetas).

%Podiamos usar ! aqui para tirar os \+
procuraEstafetaLivreEnc(_, _, []).
procuraEstafetaLivreEnc(EncId, _, [Est1|T]) :-  tamLista(T, 0),evolucao(atribuido(Est1, EncId)).
procuraEstafetaLivreEnc(EncId, Data, [Est1|T]) :- \+ tamLista(T, 0), estafetaLivre(Est1, Data),evolucao(atribuido(Est1, EncId)).
procuraEstafetaLivreEnc(EncId, Data, [Est1|T]) :- \+ tamLista(T, 0), \+ estafetaLivre(Est1, Data),procuraEstafetaLivreEnc(EncId, Data, T).


removeOneList([], _, []).
removeOneList([X|T], L2, Result):- member(X, L2), !, removeOneList(T, L2, Result). 
removeOneList([X|T], L2, [X|Result]):- removeOneList(T, L2, Result).