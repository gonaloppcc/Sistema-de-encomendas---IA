% Objetivo: Entregar todas as encomendas que ainda foram entregues.

% Entrega todas as encomendas que não tenham sido entregues
entregaEncomendas(Encs) :- 
    findall(encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), 
    (encomenda(Id, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), \+ entrega(_, _, Id, _, _, _)),
    Encs), % Todas as encomendas não entregues.
    maplist(entregaEncomenda, Encs, V).

entregaEncomenda(encomenda(EncomendaID, ClienteID , Peso, Volume, PrazoEntrega, HorasPrazoEntrega, DataDeEncomenda, HorasDataEncomenda, Rua), V) :-
    random(0, 4, EstafetaID),
    Veiculo = carro,
    random(0, 5, Rating),
    DataEntrega = data(27, 11, 2021),
    HoraEntrega = hora(23, 40),
    evolucao(entrega(EstafetaID, carro, EncomendaID, Rating, DataEntrega, HoraEntrega)).
    %assert(entrega(EstafetaID, carro, EncomendaID, Rating, DataEntrega, HoraEntrega)).

/**
Diz quais os estafetas que podem entregar a partir do ID da Encomenda. Se a encomenda sair da Póvoa de Varzim, retorna os estafetas sediados nessa cidade.
*/
filtraCidadeEncomenda(EncomendaID, ListaEstafetas) :-
    encomenda(EncomendaID, ClienteID, Peso, V, Pra, Hor, DataEnc, HoraEnc, RuaId),
    rua(RuaId, City, _),
    findall(IdsEstafetas, estafeta(IdsEstafetas, _, City), ListaEstafetas). 

/*
Verifica se um dado estafeta está livre nesse dia
Fiz em função das atribuições, e da data de entrega da encomenda. A melhor versão desta função verificaria os dias de intervalo entre a data de encomenda e a data de entrega.
E veria se ele está livre num desses dias.


Coisas que a função faz:
Procuras todas as encomendas atribuídas a esse estafeta.
Guarda as datas de entregas dessas encomendas, e filtra (com o include) quais as que coincidem com esse dia.
*/
estafetaLivre(EstafetaId, Data) :-
    findall(IdsEncomendas, atribuido(EstafetaID, IdsEncomendas), ListaEncomendas),
    verificaListaEncomendasQuantasNumDia(ListaEncomendas, Data, PesoNumDia),
    PesoNumDia =< 80.


getDataFromEncomenda(EncomendaId, DataDessaEncomenda) :- encomenda(EncomendaId, _, _, _, DataDessaEncomenda, _, _, _, _ ).
/*
Diz quantas encomendas estão planeadas para ser entregues num dado dia - data(dia, mes, ano).
A linha do maplist converte Id's de encomendas em datas.
*/
verificaListaEncomendasQuantasNumDia(Lista, Data, PesoNumDia) :-
    fazParesDataPeso_DeIdsEncomendas(Lista, ListaPares),
    %maplist(getDataFromEncomenda, Lista, Datas),
    include(comparaDatas(Data), ListaPares, DatasIguaisADada ),
%Mas o critério é o peso total das encomendas desse dia
    sumPair(DatasIguaisADada, PesoNumDia).

fazParesDataPeso_DeIdsEncomendas([], []).
fazParesDataPeso_DeIdsEncomendas([IdEncomenda|Resto], Pares) :-
    encomenda(IdEncomenda, _, Peso, V, Data, _, DataEnc, _, _),
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
    listaEncomendasNAtribuida(Lista).
    gerarAtribuicoesLista(Lista).

listaEncomendasNAtribuida(Res) :-
    findall(EncId, encomenda(EncId, _, _, _, _, _, _, _, _), ListaIDs ),
    findall(EncE, atribuido(_, EncE), ListaAtribuidas ),
    removeOneList(ListaIDs, ListaAtribuidas, Res).

gerarAtribuicoesLista([]).
gerarAtribuicoesLista([EncID|T]) :- geraUmaAtribuicao(EncID), gerarAtribuicoesLista(T).

geraUmaAtribuicao(EncId) :-
    filtraCidadeEncomenda(EncID, ListaEstafetas),
    getDataFromEncomenda(EncID, Data),
    procuraEstafetaLivreEnc(EncId, Data, ListaEstafetas).

%Podiamos usar ! aqui para tirar os \+
procuraEstafetaLivreEnc(EncId, _, []):- write("0").
procuraEstafetaLivreEnc(EncId, _, [Est1|T]) :-  tamLista(T, 0), write("1"),evolucao(atribuido(Est1, EncId)).
procuraEstafetaLivreEnc(EncId, Data, [Est1|T]) :- \+ tamLista(T, 0), estafetaLivre(Est1, Data), write("2"),evolucao(atribuido(Est1, EncId)).
procuraEstafetaLivreEnc(EncId, Data, [Est1|T]) :- \+ tamLista(T, 0), \+ estafetaLivre(Est1, Data), write("3"),procuraEstafetaLivreEnc(EncID, Data, T).



removeOneList([], _, []).
removeOneList([X|T], L2, Result):- member(X, L2), !, removeOneList(T, L2, Result). 
removeOneList([X|T], L2, [X|Result]):- removeOneList(T, L2, Result).