
import logging
from math import inf

from Fase2.algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from Fase2.base_conhecimento.baseConhecimento import transportes, encomendas

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico
flag_ecologico_ou_rapido = True


# Função para escolhermos qual o veículo a usar em função da flag e do circuito.
def veiculo_mais_ecologico(distancia_caminho, peso_total):
    """
       Usado para calcular o veículo mais ecológico para entregar uma encomenda, tendo em conta o peso.
       @param distancia_caminho: Distância usada para calcular o tempo de transporte.
       @param peso_total: Peso das encomendas desse circuito. Usado para calcular a velocidade de transporte,
       @return: Veículo mais ecológico.
       """
    melhor_coef_poluicao = float (inf)
    melhor_veiculo = None
    for veiculo in transportes:
        try:
            # Verifica se consegue transportar a encomenda.
            # Se não conseguir, tem uma exceção.
            tempo_veiculo = calcula_tempo_transporte(veiculo, peso_total, distancia_caminho)
            coef_poluicao_atual = veiculo.coeficiente_poluicao
            if coef_poluicao_atual < melhor_coef_poluicao:
                melhor_coef_poluicao = coef_poluicao_atual
                melhor_veiculo = veiculo
        except:
            pass
    return melhor_veiculo


def escolhe_veiculo(circuito):
    """
    Escolhe um veículo baseado no caminho (distância) e encomendas id (e pesos das encomendas).
    Também utilizamos a "flag" flag_ecologico_ou_rapido para saber qual o critério da escolha.
    @param circuito: Caminho para entregar a encomenda e os ids das encomendas, num par.
    @return: Veículo escolhido.
    """
    caminho, enc_ids = circuito
    logging.debug("[Gera veiculos]")
    logging.debug(f"Caminho: {caminho}")
    logging.debug(f"Encomendas: {enc_ids}")
    pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, enc_ids)
    peso_total = sum(pesos_no_percurso)

    distancia_caminho = calcula_distancia(caminho)
    if flag_ecologico_ou_rapido:
        melhor_veiculo = veiculo_mais_ecologico(distancia_caminho, peso_total)
    else:
        melhor_veiculo = veiculo_mais_rapido(distancia_caminho, peso_total)

    return melhor_veiculo


def veiculo_mais_rapido(distancia_caminho, peso_total):
    """
    Usado para calcular o veículo mais rápido a entregar uma encomenda, tendo em conta o peso.
    @param distancia_caminho: Distância usada para calcular o tempo de transporte.
    @param peso_total: Peso das encomendas desse circuito. Usado para calcular a velocidade de transporte,
    @return: Veículo mais rápido.
    """
    tempo_transporte = 100000000
    melhor_veiculo = transportes[0]
    for veiculo in transportes:
        try:
            tempo_veiculo = calcula_tempo_transporte(veiculo, peso_total, distancia_caminho)
            if tempo_veiculo < tempo_transporte:
                tempo_transporte = tempo_veiculo
                melhor_veiculo = veiculo
        except:
            pass
    return melhor_veiculo
