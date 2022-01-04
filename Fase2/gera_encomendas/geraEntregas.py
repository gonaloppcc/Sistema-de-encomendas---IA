import logging

from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, origens, transportes
from gera_encomendas.Entrega import Entrega

# TODO: Passar isto para metodos de instancia da classe Entrega?

# Variáveis globais

# Entregas realizadas
entregas = []

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico ← Falta implementar
ecologico = False


def escolhe_veiculo(cam, encomenda):
    distancia_caminho = calcula_distancia(cam)
    if not ecologico:
        tempo_transporte = float('inf')
        melhor_veiculo = transportes[0]
        for veiculo in transportes:
            try:
                tempo_veiculo = calcula_tempo_transporte(veiculo, encomenda.peso, distancia_caminho)
                logging.debug(f"escolhe_veiculo: Veiculo: {veiculo.nome}")
                logging.debug(f"escolhe_veiculo: Tempo: {tempo_veiculo:.3f}")
                if tempo_veiculo < tempo_transporte:
                    tempo_transporte = tempo_veiculo
                    melhor_veiculo = veiculo
            except:
                pass
        return melhor_veiculo


# Gera uma entrega a partir da atribuição
def gerar_entrega(atribuicao, algoritmo):  # Algoritmo usado para a procura do caminho
    estafeta = estafetas.get(atribuicao.estafeta_id)
    encomenda = encomendas.get(atribuicao.encomenda_id)
    cidade_encomenda = Local.encontra_local(encomenda.id_local_entrega).freguesia

    if estafeta.cidade is not cidade_encomenda:
        logging.error("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = Local.encontra_local(encomenda.id_local_entrega)

    logging.debug(f"estafeta.cidade: {estafeta.cidade} local_entrega: {local_entrega}")
    cam = algoritmo(origens.get(estafeta.cidade), local_entrega)

    veiculo = escolhe_veiculo(cam, encomenda)
    logging.info(f"Veículo escolhido: {veiculo}")

    return Entrega(atribuicao.encomenda_id, atribuicao.estafeta_id, 0, veiculo, cam)


# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas(algoritmo):
    for atribuicao in atribuicoes:
        logging.debug(f"Atribuição: {atribuicao} Algoritmo: {algoritmo}")
        entrega = gerar_entrega(atribuicao, algoritmo)
        if entrega is not None:
            entregas.append(entrega)
            entrega.imprime_entrega()
