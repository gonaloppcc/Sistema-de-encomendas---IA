%Datas
%data(Dia, Mes, Ano).
%Calcula intervalo de tempo entre duas datas
%Devolve em termos de dias , Minutos
intervaloTempo(data(Dia1, Mes1, Ano1), hora(H1, M1), data(Dia2, Mes2, Ano2), hora(H2, M2), DiasRes, Minutos) :- 
    DiaEntrega is Dia2-Dia1,
    MesEntrega is Mes2-Mes1,
    AnoEntrega is Ano2-Ano1,
    DiasRes is DiaEntrega+MesEntrega*30+AnoEntrega*365,
    Minutos is H2*60+M2-H1*60-M1 
    .

estaEntreDuasDatas((D1, D2), entrega(_, _, _, _, Data, _), _) :-
    estaEntreDuasDatas(D1, D2, Data).

estaEntreDuasDatas(data(Dia1, Mes1, Ano1), data(Dia2, Mes2, Ano2), data(Diat, Mest, Anot)) :-
    Ano1 =< Anot,
    Anot =< Ano2,
    Mes1 =< Mest , Mest =<  Mes2,
    Dia1 =< Diat , Diat =<  Dia2, !
    .

%estaEntreDuasDatas(data(_,_,Ano1), data(_,_,Ano2), data(_,_,Anot)) :-
%    Ano1 < Anot,
%    Anot < Ano2.
%
estaEntreDuasDatas(data(_,_,Ano1), data(_,_,Ano2), data(_,_,Anot)) :-
    Ano1 =< Anot,
    Anot < Ano2, !.

estaEntreDuasDatas(data(_,_,Ano1), data(_,_,Ano2), data(_,_,Anot)) :-
    Ano1 < Anot,
    Anot =< Ano2, !.

%Validação das datas
data(D, 1, A) :- D =< 31, D > 0,  A> 0.
data(D, 2, A) :- D < 30, D > 0,  A> 0.
data(D, 3, A) :- D =< 31, D > 0, A> 0.
data(D, 4, A) :- D < 31, D > 0, A> 0.
data(D, 5, A) :- D =< 31, D > 0, A> 0.
data(D, 6, A) :- D < 31, D > 0,  A> 0.
data(D, 7, A) :- D =< 31, D > 0,  A> 0.
data(D, 8, A) :- D =< 31, D > 0,  A> 0.
data(D, 9, A) :- D < 31, D > 0,  A> 0.
data(D, 10, A) :- D =< 31, D > 0,  A> 0.
data(D, 11, A) :- D < 31, D > 0,  A> 0.
data(D, 12, A) :- D =< 31, D > 0,  A> 0.

hora(H,M) :- 
    H < 24,
    H >= 0,
    M < 60,
    M >= 0
. 

%Funções
%Compara duas datas
comparaDatas(data(D1, M1, A1), data(D1, M1, A1)).
comparaDatas(data(D1, M1, A1), (data(D1, M1, A1), _)).