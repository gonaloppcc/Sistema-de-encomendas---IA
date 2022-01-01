class Local:
    def __init__(self, id_: int, freguesia, nome):
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
