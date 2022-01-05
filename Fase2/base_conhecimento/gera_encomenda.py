from datetime import date, timedelta
from random import randint

from algoritmos_procura.common import maximo_peso_uma_viagem
from base_conhecimento.Encomenda import Encomenda
from base_conhecimento.baseConhecimento import id_locais_cidades, encomendas, origens


def gera_encomendas(num_encomendas, nome_cidade):
    """
    Função que gera encomendas para uma cidade. A variação da data de encomenda varia 1 dia da data atual,
    e o peso também é aleatório, entre 1 e o máximo que é possível transportar.
    @param num_encomendas: número de encomendas para serem geradas.
    @param nome_cidade: Qual a cidade de destino das encomendas geradas.
    """
    peso_maximo = maximo_peso_uma_viagem()
    data_encomenda_hoje = date.today()
    if len(encomendas) == 0:
        id_encomenda_atual = 0
    else:
        id_encomenda_atual = encomendas.keys().max() + 1
    for encomenda_id in range(id_encomenda_atual, id_encomenda_atual + num_encomendas):
        peso = randint(1, peso_maximo)
        data_encomenda_aleatoria = data_encomenda_hoje + timedelta(days=randint(-1, 1))
        id_inicio, id_fim = id_locais_cidades.get(nome_cidade)
        id_local_entrega = randint(id_inicio + 1, id_fim - 1)
        while id_local_entrega == origens.get(nome_cidade):
            id_local_entrega = randint(id_inicio + 1, id_fim - 1)
        # encomenda_id, cliente_id, peso,  volume, prazo data_encomenda,         id_local_entrega
        nova_encomenda = Encomenda(encomenda_id, 0, peso, 0, data_encomenda_aleatoria + timedelta(days=2),
                                   data_encomenda_aleatoria, id_local_entrega)
        encomendas[encomenda_id] = nova_encomenda
