# Estafetas
# São caraterizados por um ID, um nome, e um posto de distribuição, cidade.
# A cidade é uma ‘string’, e é o segundo parâmetro de um Local
class Estafeta:
    def __init__(self, estafeta_id, nome, cidade):
        self.estafeta_id = estafeta_id
        self.nome = nome
        self.cidade = cidade
    # Este estafeta entrega no grafo atual
