# Class Transporte:
# Transportes e velocidade, temos tudo em km/h


class Transporte:
    def __init__(self, nome: object, peso_maximo: int, velocidade_max: int, coeficiente_kg_velocidade: float,
                 preco_km: int):
        """
        Construtor do tipo transporte.
        @param nome: Nome do transporte.
        @param peso_maximo: Peso máximo que o transporte pode transportar.
        @param velocidade_max: Velocidade máxima que o veículo pode ter.
        @param coeficiente_kg_velocidade: Coeficiente que descreve quão afetada é a velocidade em função do peso transportado.
        @param preco_km:
        """
        self.nome = nome
        self.peso_maximo = peso_maximo
        self.velocidade_max = velocidade_max
        self.coeficiente_kg_velocidade = coeficiente_kg_velocidade
        self.preco_km = preco_km

    def calcula_velocidade(self, peso_encomenda: int) -> int:
        """
        Calcula a velocidade que um veículo consegue atingir a partir do peso da encomenda que irá transportar.
        Utilizamos o coeficiente_kg_velocidade.
        @param peso_encomenda: Peso da encomenda que será transportada.
        @return: Velocidade média durante a entrega da encomenda.
        """
        if peso_encomenda > self.peso_maximo:
            return 0
        penalizacao_peso = self.coeficiente_kg_velocidade * peso_encomenda
        return self.velocidade_max - penalizacao_peso
