class Local:

   
       #Falta acrescentar os floats

    def __init__(self, id_: int, freguesia, nome, x: float, y: float):
        """
        Construtor dos vários pontos que compões uma cidade.
        @param id_: Id único que identifica os pontos de entrega de cada encomenda.
        @param freguesia: Cidade a que pertence o local, para podermos ter centros de entrega em várias cidades. (string)
        @param nome: Nome do local, para ser mais legível quando quisermos analisar este local. (string)
        """
        self.id = id_
        self.freguesia = freguesia
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return self.nome
