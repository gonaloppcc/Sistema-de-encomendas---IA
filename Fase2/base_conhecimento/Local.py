class Local:

    def __init__(self, id_: int, freguesia, nome, x: float, y: float):
        """
        Construtor dos vários pontos que compões uma cidade.
        @param id_: Id único que identifica os pontos de entrega de cada encomenda.
        @param freguesia: Cidade a que pertence o local, para podermos ter centros de entrega em várias cidades. (string)
        @param nome: Nome do local, para ser mais legível quando quisermos analisar este local. (string)
        @param x: Coordenadas das abcissas do local na freguesia.
        @param y: Coordenadas das ordenadas do local na freguesia.

        """
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return self.nome

    @staticmethod
    def encontra_local(id_local: int):
        from base_conhecimento.baseConhecimento import mapa
        mapa
        for grafo in mapa["grafos"].values():
            for local in grafo:
                if local.id == id_local:
                    return local
        return None

    def encontra_cidade(self):
        """
        Encontra a cidade a que pertence um local.
        @return: Nome da cidade.
        """
        return self.encontra_local(self.id).freguesia
