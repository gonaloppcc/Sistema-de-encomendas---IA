from random import randint

from base_conhecimento.Estafeta import Estafeta
from base_conhecimento.baseConhecimento import estafetas

nomes_possiveis_estafeta = ["Marco", "Gonçalo", "Rita", "Diogo"]


def gerar_estafeta(cidade_destino):
    """
    Função que gera um estafeta para uma cidade.
    @param cidade_destino: Cidade na qual o estafeta deve fazer entregas.
    @return: Estafeta criado.
    """
    max_id_estafeta = 1
    for _, estafeta in estafetas.items():
        if estafeta.estafeta_id > max_id_estafeta:
            max_id_estafeta = estafeta.estafeta_id
    max_id_estafeta += 1
    nome_estafeta = nomes_possiveis_estafeta[randint(0, len(nomes_possiveis_estafeta)) - 1]
    estafeta_novo = Estafeta(max_id_estafeta, nome_estafeta, cidade_destino)
    estafetas[cidade_destino] = estafeta_novo
    return estafeta_novo
