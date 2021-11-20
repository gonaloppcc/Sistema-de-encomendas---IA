% Objetivo da Empresa Green Distribution -> Privilegiar sempre o meio de transporte + ecológico

% Todos os id's usados devem ser únicos! De forma a que a unificação só ocorra uma vez no máximo para um id.

% 1. Definição das ruas de uma freguesia
%rua(id, freguesia, nome, ...). % Como é que definimos?
rua(1, vilaDoConde, rua1). 


% 2. Definição do cliente
%cliente(id, nome).
cliente(1, marco).


% 3. Definição da encomenda
%encomenda(clienteID, peso, volume, prazoEntrega, dataDeEncomenda, ruaEntrega). % Vai ser atribuido a um estafeta // dataDeEncomenda -> Data em que foi efetuada a encomenda pelo cliente
%                                   dias/horas, hora/min/dia/mes/ano
encomenda(1, 20, 25, 0/24, 16/43 / 08/08/2021, 1).


% 4. Definição do estafeta
%estafeta(id, nome, rating).
estafeta(1, diogo, 4).

% Prazo não cumprido por parte do estafeta -> Diminuir o seu número de entregas

% 0 <= Rating <= 5


% 5. Definição preço de entrega
preco(Encomenda, TransporteUtilizado, P) :- P is Encomenda * TransporteUtilizado.


% 6. Meios de transporte
%transporte(nome, pesoMaximo, velMax).
transporte(bicicleta, 5, 10).
transporte(moto, 20, 35).
transporte(carro, 100, 25).

% Meio de Transporte        Peso máximo das encomendas (Kg)        Velocidade Máxima (Km/h)
% Bicicleta                 5                                      10                           
% Moto                      20                                     35
% Carro                     100                                    25

% -> Vertente Ecológica dos meios de transporte pode ser descrita através de uma lista ordenada.
% Em que o primeiro elemento da lista pode ser, por exemplo, o mais ecológico e assim em diante...
ecologicos([bicicleta, moto, carro]).


% Falta resumir os objetivos/queries aqui
%
% Query 1
% Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
estafetaMaisEcologico(Estafeta) :- findAll(estafeta, ,
                                  include(estafeta).
%
%
%
