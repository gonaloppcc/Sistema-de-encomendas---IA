% Objetivo da Empresa Green Distribution -> Privilegiar sempre o meio de transporte + ecológico

% Todos os ids usados devem ser únicos! De forma a que a unificação só ocorra uma vez no maximo para um id.

:- include('baseConhecimento.pl').

%Atribuir ratings
estafetaEntregaSucesso(estafeta(Id, Nome, 5), estafeta(Id, Nome, 5)):- !.
estafetaEntregaSucesso(estafeta(Id, Nome, Rating), estafeta(Id, Nome, RatingNovo)) :- RatingNovo is Rating+1.


estafetaEntregaFalhou(estafeta(Id, Nome, 0), estafeta(Id, Nome, 0)):- !.
estafetaEntregaFalhot(estafeta(Id, Nome, Rating), estafeta(Id, Nome, RatingNovo)) :- RatingNovo is Rating-1.
% Prazo não cumprido por parte do estafeta -> Diminuir o seu número de entregas

% 0 <= Rating <= 5


% 5. Definição preço de entrega
preco(Encomenda, TransporteUtilizado, P) :- P is Encomenda * TransporteUtilizado.


% 6. Meios de transporte

%Deviamos escolher um limite de horas de trabalho por dia
%Porque ele não passa 24 horas na estrada
calculaVelocidade(Distancia, data(Dia, Mes, Ano), Velocidade) :-
    Horas is Dia*24+Mes*30*24+Ano*365*24,
    Velocidade is Horas/Distancia.

descobreCidade(Id, Cidade) :-
    rua(Id, Cidade, _).

distanciaPorRua(Rua, CidadeDest, Res) :-
    descobreCidade(Rua, CidadeOrigem),
    distancia(CidadeDest, CidadeOrigem, Res).

decideTransporte(_, encomenda(_, Peso, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, Peso, Data1, Data2, _, Rua), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distanciaPorRua(Rua, Cidade, Distancia),
    velocidadeEntrega is DataEntrega/Distancia,
    velocidadeEntrega < 10.
    

%Decide meio transporte
decideTransporte(_, encomenda(_, Peso, _, _, _, _), transporte(carro, 100, 25)) :- Peso > 20.
decideTransporte(estafeta(_, _, _, Cidade), encomenda(_, Peso, Data1, Data2, _, Rua), transporte(bicicleta, 5, 10)) :-
    intervaloTempo(Data1, Data2, DataEntrega),
    distancia(Rua, Cidade, Distancia),
    velocidadeEntrega is DataEntrega/Distancia,
    velocidadeEntrega < 10.
    
% -> Vertente Ecológica dos meios de transporte pode ser descrita através de uma lista ordenada.
% Em que o primeiro elemento da lista pode ser, por exemplo, o mais ecológico e assim em diante...
ecologicos([bicicleta, moto, carro]).


%Datas
data(Dia, Mes, Ano).
%Calcula intervalo de tempo entre duas datas
intervaloTempo(data(Dia1, Mes1, Ano1), data(Dia2, Mes2, Ano2), data(DiaEntrega, MesEntrega, AnoEntrega)) :- 
    DiaEntrega is Dia2-Dia1,
    MesEntrega is Mes2-Mes1,
    AnoEntrega is Ano2-Ano1.


clientes_entregues([],R,L).
clientes_entregues([encomenda(Cliente,_,_,_,_)|T], R, L) :-
    not(member(Cliente,L)),
    clientes_entregues(T,L)
.
clientes_entregues([encomenda(Cliente,_,_,_,_)|T], R, L) :-
    clientes_entregues(T,R,L)
.

/* 
*  Conta o número de vezes que cada estafeta utilizou cada veículo retornando uma lista com esta ordem Bicicleta, Mota, Carro
*
*  1º: Lista de entregas do estafeta
*  2º: Número de vezes que utilizou bicicleta
*  3º: Número de vezes que utilizou moto
*  4º: Número de vezes que utilizou carro
*/
contaVeiculos([],0,0,0).
contaVeiculos([entrega(_,bicicleta,_,_,_)|T], NovoNBicla, NMoto, NCarro) :-
    contaVeiculos(T, NBicla, NMoto, NCarro),
    NovoNBicla is NBicla + 1
.
contaVeiculos([entrega(_,moto,_,_,_)|T], NBicla, NovoNMoto, NCarro) :-
    contaVeiculos(T, NBicla, NMoto, NCarro),
    NovoNMoto is NMoto + 1
.
contaVeiculos([entrega(_,carro,_,_,_)|T], NBicla, NMoto, NovoNCarro) :-
    contaVeiculos(T,NBicla,NMoto,NCarro),
    NovoNCarro is NCarro + 1
.

/*
*  Vê dos dois estafetas tem maior nº de usos e retorna o maior...
*
*  1º: (ID do estafeta)                                       /    (Nº de vezes que utilizou o veículo)
*  2º: (ID do outro estafeta)                                 /    (Nº de vezes que utilizou o veículo)
*  3º: (ID do estafeta que utilizou mais vezes o veículo)     /    (Nº de vezes que utilizou o veículo)
*/
veMaior(ID1/N1, ID2/N2, ID1/N1) :- N1 > N2.
veMaior(ID1/N1, ID2/N2, ID2/N2) :- N2 >= N1.