import sys

from algoritmosProcura.common import print_caminho, calcula_distancia, calcula_tempo_transporte
from algoritmosProcura.dfs import dfs, bfs, dfsLimited
from baseConhecimento import atribuicoes, estafetas, encomendas, locais, origens, transportes

#Variáveis globais

#Entregas realizadas
entregas_feitas = []

#Se for falsa, queremos o mais rápido, logo é carro
#Se for verdadeira, tem de ser o mais ecológico <- Falta implementar
flag_ecologico_ou_rapido = False

#Entrega
#Regista as seguintes informações:
# Id da encomenda, id do estafeta, data da entrega, meio utilizado, caminho usado
class Entrega:
    def __init__(self, encomenda_id, estafeta_id, data_entrega, transporte, caminho):
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id 
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

    def imprime_entrega(self):
        print("Id da encomenda: ", self.encomenda_id)
        print("Id da estafeta: ", self.estafeta_id)
        print("Data entrega: ", self.data_entrega)
        print("Transporte: ", self.transporte.nome)
        print("Caminho feito: ")
        print_caminho(self.caminho)



def escolhe_veiculo(cam, encomenda):
    distancia_caminho = calcula_distancia(cam)
    if not flag_ecologico_ou_rapido:
        tempo_transporte = 100000000
        melhor_veiculo = transportes[0]
        for veiculo in transportes:
            try:
                tempo_veiculo = calcula_tempo_transporte(veiculo, encomenda.peso, distancia_caminho)
                #print("Passa pelo veiculo: ", veiculo.nome)
                #print("Com tempo de entrega: ", tempo_veiculo)
                if tempo_veiculo < tempo_transporte:
                    tempo_transporte = tempo_veiculo
                    melhor_veiculo = veiculo
            except:
                pass
        return melhor_veiculo

#Gera uma entrega a partir da atribuição
def gerar_entrega(atribuicao):
    estafeta_id = atribuicao.estafeta_id
    encomenda_id = atribuicao.encomenda_id
    #Dá para juntar as duas linhas de cima com as de baixo
    estafeta = estafetas.get(estafeta_id)
    encomenda = encomendas.get(encomenda_id)
    cidade_estafeta = estafeta.cidade
    cidade_encomenda = locais.get(encomenda.id_local_entrega).freguesia
    if cidade_estafeta is not cidade_encomenda:
        print("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = locais.get(encomenda.id_local_entrega)

    #Para mudar o algoritmo é aqui

    cam = dfs(origens.get(cidade_estafeta), local_entrega)
    veiculo = escolhe_veiculo(cam, encomenda)
    entrega_feita = Entrega(encomenda_id, estafeta_id, 0, veiculo, cam)
    return entrega_feita

#Coisas sobre este teste
#Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
#Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
#Mas a outra pesa muito para a mota, logo é o carro que leva

#Gera todas as atribuições
def gerar_entregas():
    for atribuicao in atribuicoes:
        entrega = gerar_entrega(atribuicao)
        if (entrega is not None):
            entregas_feitas.append(entrega)
            entrega.imprime_entrega()
            print("<------------------>")
