% Objetivo da Empresa Green Distribution -> Privilegiar sempre o meio de transporte + ecológico


% 1. Definição das ruas de uma freguesia
rua(freguesia, nome, ...). % Como é que definimos?


% 2. Definição do cliente
cliente(nome, listaEncomendas).


% 3. Definição da encomenda
encomenda(cliente, peso, volume, prazoEntrega). % Vai ser atribuido a um estafeta


% 4. Definição do estafeta
estafeta(nome, rating).

% Prazo não cumprido por parte do estafeta -> Diminuir o seu número de entregas

% 0 <= Rating <= 5

% 5. Definição preço de entrega
preco(encomenda, transporteUtilizado).


% Meio de Transporte        Peso máximo das encomendas (Kg)        Velocidade Máxima (Km/h)
% Bicicleta                 5                                      10                           
% Moto                      20                                     35
% Carro                     100                                    25

% -> Vertente Ecológica dos meios de transporte pode ser descrita através de uma lista ordenada.
% Em que o primeiro elemento da lista pode ser, por exemplo, o mais ecológico e assim em diante...


% Falta resumir os objetivos/queries aqui
