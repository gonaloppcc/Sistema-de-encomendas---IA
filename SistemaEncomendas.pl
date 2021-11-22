% Objetivo da Empresa Green Distribution -> Privilegiar sempre o meio de transporte + ecológico

% Todos os ids usados devem ser únicos! De forma a que a unificação só ocorra uma vez no maximo para um id.

% 1. Definição das ruas de uma freguesia
%rua(id, freguesia, nome, ...). % Como é que definimos?
rua(1, vilaDoConde, rua1). 
rua(2, povoaVarzim, rua1). 

distancia(vilaDoConde, povoa_Varzim, 10). 

% 2. Definição do cliente
%cliente(id, nome).
cliente(1, marco).


% 3. Definição da encomenda
%encomenda(encomendaID, clienteID, peso, volume, prazoEntrega, dataDeEncomenda, ruaID). % Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
%                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 1, 20, 25, data(1,1,1), data(4,5,1), 2).

%entrega(estafeta, veiculo, encomenda, dataEntrega).
entrega(1, carro, treta, rating, data(23/12/2019,18/40)).

% 4. Definição do estafeta
%Acho que é preciso atribuir a cidade de origem
%estafeta(id, nome, rating/num, cidade, nEncomendas).
estafeta(1, diogo, 4/420, povoaVarzim, 2).

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
%transporte(nome, pesoMaximo, velMax).
transporte(bicicleta, 5, 10).
transporte(moto, 20, 35).
transporte(carro, 100, 25).

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
    


% Meio de Transporte        Peso maximo das encomendas (Kg)        Velocidade Máxima (Km/h)
% Bicicleta                 5                                      10                           
% Moto                      20                                     35
% Carro                     100                                    25

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


% Falta resumir os objetivos/queries aqui
%
% Query 1
% Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
estafetaMaisEcologico(Estafeta) :- findAll(estafeta, include(estafeta)).
%
%
%




l([1/[encomenda(2,qw,eqw,ads,asd,ads)], 2/[encomenda(3,lkj,kink,ads,çoadj,123)]]).

% L = lista com pares(idEstafeta,Entregas).
estafeta_clientes(ID, [ID/entregas|T], Clientes) :-
    clientes_entregues(entregas, Clientes)
.
estafeta_clientes(ID, [ID2/entregas|T], Clientes) :-
    ID \= ID2,
    estafeta_clientes(ID,T,Clientes)
.

clientes_entregues([],R,L).
clientes_entregues([encomenda(Cliente,_,_,_,_)|T], R, L) :-
    not(member(Cliente,L)),
    clientes_entregues(T,[Cliente|R],L)
.
clientes_entregues([encomenda(Cliente,_,_,_,_)|T], R, L) :-
    clientes_entregues(T,R,L)
.