%Datas
%data(Dia, Mes, Ano).
%Calcula intervalo de tempo entre duas datas
intervaloTempo(data(Dia1, Mes1, Ano1), data(Dia2, Mes2, Ano2), data(DiaEntrega, MesEntrega, AnoEntrega)) :- 
    DiaEntrega is Dia2-Dia1,
    MesEntrega is Mes2-Mes1,
    AnoEntrega is Ano2-Ano1.


estaEntreDuasDatas(data(Dia1, Mes1, Ano1), data(Dia2, Mes2, Ano2), data(Diat, Mest, Anot)) :-
    Ano1 =< Anot,
    Anot =< Ano2,
    Mes1 =< Mest , Mest =<  Mes2,
    Dia1 =< Diat , Diat =<  Dia2
    .

estaEntreDuasDatas(data(Dia1, Mes1, Ano1), data(Dia2, Mes2, Ano2), data(Diat, Mest, Anot)) :-
    Ano1 < Anot,
    Anot < Ano2.

%Isto não está a verificar
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

