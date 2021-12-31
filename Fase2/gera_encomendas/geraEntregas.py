from gera_encomendas.Entrega import Entrega
from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from algoritmos_procura.dfs import dfs
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, locais, origens, transportes

# TODO: Passar isto para metodos de instancia da classe Entrega?

# Variáveis globais

# Entregas realizadas
entregas_feitas = []

# Se for falsa, queremos o mais rápido, logo é carro
# Se for verdadeira, tem de ser o mais ecológico ← Falta implementar
flag_ecologico_ou_rapido = False

#Escolhe o veículo que pode entregar uma encomenda.
#Recebe o caminho e a encomenda, e a partir do peso vê qual o melhor veículo para a entregar.
#Para já, só vê em função da velocidade, falta ver um critério para o ser "verde".
def escolhe_veiculo(cam, encomenda):
    distancia_caminho = calcula_distancia(cam)
    if not flag_ecologico_ou_rapido:
        tempo_transporte = 100000000
        melhor_veiculo = transportes[0]
        for veiculo in transportes:
            try:
                tempo_veiculo = calcula_tempo_transporte(veiculo, encomenda.peso, distancia_caminho)
                # print("Passa pelo veiculo: ", veiculo.nome)
                # print("Com tempo de entrega: ", tempo_veiculo)
                if tempo_veiculo < tempo_transporte:
                    tempo_transporte = tempo_veiculo
                    melhor_veiculo = veiculo
            except:
                pass
        return melhor_veiculo


# Gera uma entrega a partir da atribuição
def gerar_entrega(atribuicao):
    estafeta_id = atribuicao.estafeta_id
    encomenda_id = atribuicao.encomenda_id
    # Dá para juntar as duas linhas de cima com as de baixo
    estafeta = estafetas.get(estafeta_id)
    encomenda = encomendas.get(encomenda_id)
    cidade_estafeta = estafeta.cidade
    cidade_encomenda = locais.get(encomenda.id_local_entrega).freguesia
    if cidade_estafeta is not cidade_encomenda:
        print("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = locais.get(encomenda.id_local_entrega)

    # Para mudar o algoritmo é aqui

    cam = dfs(origens.get(cidade_estafeta), local_entrega)
    veiculo = escolhe_veiculo(cam, encomenda)
    entrega_feita = Entrega(encomenda_id, estafeta_id, 0, veiculo, cam)
    return entrega_feita

#Descobre todas as encomendas que um dado estafeta deve fazer
def entregas_do_estafeta(estafeta):
    list_encomendas = []
    for atribuicao1 in atribuicoes:
        if atribuicao1.estafeta_id == estafeta:
            list_encomendas.append(atribuicao1.encomenda_id)
    return list_encomendas


"""
Esta função recebe qual é o estefeta que vamos analisar, e devolve uma lista de listas com as possíveis entregas que ele pode fazer.
Por exemplo, se o estafeta 1 tiver que entregas a encomenda A, B e C, ele vai devolver a seguinte lista:
[
[[A], [B], [C]], 
[[A, B], [C]],
[[A], [B, C]],
[[A, B, C]],
]
Como cada estefeta só entrega na sua cidade, vamos procurar todos os possíveis percursos, independentemente do custo.
"""
def descobre_possiveis_caminhos(encomendasID):
    locais_entrega = map(lambda encomendaID: encomendas.get(encomendaID).id_local_entrega, encomendasID)
    


# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas():
    lista_estafetas = {atribuicao.estafeta_id for atribuicao in atribuicoes}

    for estafeta in lista_estafetas:
        print("Vamos analisar o estafeta nr.: ", estafeta)
        encomendasID = entregas_do_estafeta(estafeta)
        print("ID's das encomendas que tem para entregar: ", encomendasID)

        possiveis_percursos = descobre_possiveis_caminhos(encomendasID)


        entrega = gerar_entrega(atribuicao)
        if entrega is not None:
            entregas_feitas.append(entrega)
            entrega.imprime_entrega()
            print("<------------------>")
""" Versão ANTIGA
    for atribuicao in atribuicoes:
        entrega = gerar_entrega(atribuicao)
        if entrega is not None:
            entregas_feitas.append(entrega)
            entrega.imprime_entrega()
            print("<------------------>")
            """