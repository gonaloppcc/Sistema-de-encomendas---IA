class Local:
    def __init__(self, id_: int, freguesia, nome):
        """
        Construtor dos vários pontos que compões uma cidade.
        @param id_: Id único que identifica os pontos de entrega de cada encomenda.
        @param freguesia: Cidade a que pertence o local, para podermos ter centros de entrega em várias cidades. (string)
        @param nome: Nome do local, para ser mais legível quando quisermos analisar este local. (string)
        """
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome
