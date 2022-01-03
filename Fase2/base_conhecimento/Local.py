class Local:
    def __init__(self, id_: int, freguesia, nome, x: float, y: float):
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return self.nome
