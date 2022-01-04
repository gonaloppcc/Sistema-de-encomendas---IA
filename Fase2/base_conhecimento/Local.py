from base_conhecimento import baseConhecimento


class Local:
    def __init__(self, id_: int, freguesia, nome, x: float, y: float):
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return self.nome

    @staticmethod
    def encontra_local(id_local: int):
        for grafo in baseConhecimento.mapa["grafos"].values():
            for local in grafo:
                if local.id == id_local:
                    return local
        return None
