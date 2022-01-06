from base_conhecimento.baseConhecimento import encomendas, estafetas, atribuicoes
from base_conhecimento.entidades.Atribuicao import Atribuicao
from gera_conhecimento.gera_estafeta import gerar_estafeta


def gera_atribuicoes():
    """
    Função que gera atribuições para encomendas que ainda não foram atribuídas a nenhum estafeta.
    """
    encomendas_atribuidas = {-1}
    for atribuicao in atribuicoes:
        encomendas_atribuidas.add(atribuicao.encomenda_id)
    for encomenda_id in encomendas:
        if encomenda_id not in encomendas_atribuidas:
            encomenda = encomendas.get(encomenda_id)
            cidade_destino = encomenda.cidade_encomenda()
            estafeta = estafetas.get(cidade_destino)
            if estafeta is None:
                estafeta = gerar_estafeta(cidade_destino)
            atribuicao_nova = Atribuicao(estafeta.estafeta_id, encomenda_id)
            atribuicoes.append(atribuicao_nova)
