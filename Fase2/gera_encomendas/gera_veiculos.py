# Escolhe o veículo que pode entregar uma encomenda.
# Recebe o caminho e a encomenda, e a partir do peso vê qual o melhor veículo para a entregar.
# Para já, só vê em função da velocidade, falta ver um critério para o ser "verde".
from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from base_conhecimento.baseConhecimento import transportes, encomendas

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico ← Falta implementar
flag_ecologico_ou_rapido = False


# Função para escolhermos qual o veículo a usar em função da flag e do circuito.
def escolhe_veiculo(circuito):
    caminho, enc_ids = circuito
    print("[Gera veiculos]")
    print("Caminho: ", caminho)
    print("Encomendas: ", enc_ids)
    pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, enc_ids)
    peso_total = sum(pesos_no_percurso)

    distancia_caminho = calcula_distancia(caminho)
    if not flag_ecologico_ou_rapido:
        tempo_transporte = 100000000
        melhor_veiculo = transportes[0]

        for veiculo in transportes:
            try:
                tempo_veiculo = calcula_tempo_transporte(veiculo, peso_total, distancia_caminho)
                # print("Passa pelo veiculo: ", veiculo.nome)
                # print("Com tempo de entrega: ", tempo_veiculo)
                if tempo_veiculo < tempo_transporte:
                    tempo_transporte = tempo_veiculo
                    melhor_veiculo = veiculo
            except:
                pass
        return melhor_veiculo
