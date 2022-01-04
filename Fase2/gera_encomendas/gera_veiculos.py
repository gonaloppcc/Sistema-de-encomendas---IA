# Escolhe o veículo que pode entregar uma encomenda.
# Recebe o caminho e a encomenda, e a partir do peso vê qual o melhor veículo para a entregar.
# Para já, só vê em função da velocidade, falta ver um critério para o ser "verde".
import logging

from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from base_conhecimento.baseConhecimento import transportes, encomendas

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico ← Falta implementar
flag_ecologico_ou_rapido = True


# Função para escolhermos qual o veículo a usar em função da flag e do circuito.
def veiculo_mais_ecologico(distancia_caminho, peso_total):
    """
       Usado para calcular o veículo mais ecológico para entregar uma encomenda, tendo em conta o peso.
       @param distancia_caminho: Distância usada para calcular o tempo de transporte.
       @param peso_total: Peso das encomendas desse circuito. Usado para calcular a velocidade de transporte,
       @return: Veículo mais ecológico.
       """
    melhor_coef_poluicao = transportes[0].coeficiente_poluicao
    melhor_veiculo = transportes[0]
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