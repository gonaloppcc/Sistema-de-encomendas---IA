# Estafetas
# São caraterizados por um ID, um nome, e um posto de distribuição, cidade.
# A cidade é uma ‘string’, e é o segundo parâmetro de um Local
import string


class Estafeta:
    def __init__(self, estafeta_id: int, nome: object, cidade: string):
        """
        Construtor do estafeta.
        @param estafeta_id: Id único que identifica o estafeta nas atribuições.
        @param nome: Nome do estafeta (string).
        @param cidade: Cidade do estafeta. Usada para calcular o ponto de partida das entregas (string).
        """
        self.estafeta_id = estafeta_id
        self.nome = nome
        self.cidade = cidade

    @staticmethod
    def get_nome_estafeta(id_estafeta):
        """
        Descobre o nome do estafeta en função do id.
        @param id_estafeta: Id do estafeta.
        @return: Nome do estafeta
        """
        from base_conhecimento.baseConhecimento import estafetas
        for _, estafeta in estafetas.items():
            if estafeta.estafeta_id == id_estafeta:
                return estafeta.nome
        #return "Zé"