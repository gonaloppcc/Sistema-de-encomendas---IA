import logging

from gera_encomendas.Entrega import Entrega
from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from algoritmos_procura.dfs import dfs, bfs
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, locais, origens, transportes

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
                logging.info("Passa pelo veiculo: ", veiculo.nome)
                logging.info("Com tempo de entrega: ", tempo_veiculo)
                print('ola')
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
    cidade_encomenda = locais.get(encomenda.id_local_entrega).freguesia

    if estafeta.cidade is not cidade_encomenda:
        logging.error("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = locais.get(encomenda.id_local_entrega)

    # Para mudar o algoritmo é aqui

    cam = algoritmo(origens.get(estafeta.cidade), local_entrega)
    veiculo = escolhe_veiculo(cam, encomenda)

    return Entrega(atribuicao.encomenda_id, atribuicao.estafeta_id, 0, veiculo, cam)


# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas():
    for atribuicao in atribuicoes:
        entrega = gerar_entrega(atribuicao)
        if entrega is not None:
            entregas.append(entrega)
            entrega.imprime_entrega()
            print("<------------------>")
