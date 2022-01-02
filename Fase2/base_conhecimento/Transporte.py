# Class Transporte:
# Transportes e velocidade, temos tudo em km/h
class Transporte:
    def __init__(self, nome, peso_maximo, velocidade_max, coeficiente_kg_velocidade, preco_km):
        self.nome = nome
        self.peso_maximo = peso_maximo
        self.velocidade_max = velocidade_max
        self.coeficiente_kg_velocidade = coeficiente_kg_velocidade
        self.preco_km = preco_km

    def calcula_velocidade(self, peso_encomenda):
        if peso_encomenda > self.peso_maximo:
            return 0
        penalizacao_peso = self.coeficiente_kg_velocidade * peso_encomenda
        return self.velocidade_max - penalizacao_peso
