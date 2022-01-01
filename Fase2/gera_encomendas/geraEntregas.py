from math import inf

from algoritmos_procura.common import calcula_distancia, maximo_peso_uma_viagem, print_caminho
from base_conhecimento.baseConhecimento import atribuicoes, estafetas, encomendas, locais, origens
from gera_encomendas.Entrega import Entrega
# Entregas realizadas
from gera_encomendas.gera_caminhos import descobre_possiveis_caminhos
from gera_encomendas.gera_veiculos import escolhe_veiculo

# TODO: Passar isto para metodos de instancia da classe Entrega?
# Variáveis globais

entregas_feitas = []


# Gera uma entrega a partir da atribuição
def gerar_entrega(estafeta, encomenda):
    cidade_estafeta = estafeta.cidade
    cidade_encomenda = locais.get(encomenda.id_local_entrega).freguesia
    if cidade_estafeta is not cidade_encomenda:
        print("As cidades de encomenda e de estafetas não coincidem")
        raise Exception("Cidades não coincidem")
    local_entrega = locais.get(encomenda.id_local_entrega)

    # Para mudar o algoritmo é aqui

    # cam = dfs(origens.get(cidade_estafeta), local_entrega)
   # veiculo = escolhe_veiculo(cam, encomenda)
   # entrega_feita = Entrega(encomenda.encomenda_id, estafeta.estafeta_id, 0, veiculo, cam)
   # return entrega_feita


# Descobre todas as encomendas que um dado estafeta deve fazer, pelas atribuições
def entregas_do_estafeta(estafeta):
    list_encomendas = []
    for atribuicao1 in atribuicoes:
        if atribuicao1.estafeta_id == estafeta:
            list_encomendas.append(atribuicao1.encomenda_id)
    return list_encomendas



#Descobre os ids das encomendas que são entregues num dado percurso.
#Necessário para ver se é possível entregar todas as encomendas associadas a esse nodo
#E na parte final de gerar as entregas
def encomendas_nesse_percurso(percurso, encomendas_id):
    encomendas_id_local = []
    for id in encomendas_id:
        if encomendas.get(id).id_local_entrega in percurso:
            encomendas_id_local.append(id)
    return encomendas_id_local

#Verifica se é possível fazer o percurso associado a uma lista de destinos
# Um caminho possível é do tipo: [[A, B, C], [D]]
def possivel_por_pesos(um_caminho_possivel, encomendas_id):
    maximo_possivel = maximo_peso_uma_viagem()
    #Um exemplo dum subcaminho: [A, B, C]
    for sub_caminho in um_caminho_possivel:
        #Ids das encomendas entregues neste percurso
        encomendas_no_percurso = encomendas_nesse_percurso(sub_caminho, encomendas_id)
        #Vai buscar o peso de cada encomenda
        pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, encomendas_no_percurso)
        peso_no_sub_caminho = sum(pesos_no_percurso)
        if peso_no_sub_caminho > maximo_possivel:
            print("[geraEntregas] Um caminho foi descartado: ", peso_no_sub_caminho, " > ", maximo_possivel)
            return False
    return True

# Gera as entregas de um dado estafeta. Recebe o algoritmo usado para o cálculo dos caminhos
def gera_entrega_um_estafeta(estafeta_id, algoritmo):
    estafeta = estafetas.get(estafeta_id)
    print("Vamos analisar o estafeta nr.: ", estafeta_id)
    # Encomendas que o estafeta vai entregar
    encomendas_id = entregas_do_estafeta(estafeta_id)
    # Combinações dos possíveis caminhos que o estafeta pode usar
    possiveis_percursos = descobre_possiveis_caminhos(encomendas_id)
    # Local do centro de entregas, ele tem de partir e voltar para lá
    origem_cidade = origens.get(estafeta.cidade)

    # Guardam as melhores distâncias e caminhos
    melhor_distancia = float(inf)
    #Guarda os caminhos do melhor
    melhor_caminho = []
    #um caminho possível = [[A, B, C], [D]]
    for um_caminho_possivel in possiveis_percursos:
        #Verificamos se é possível fazer este percurso com as paragens atuais
        if possivel_por_pesos(um_caminho_possivel, encomendas_id):

            total_este_caminho = 0
            # Guarda os percursos que faz para entregar as várias encomendas
            caminhos_pos_algoritmos = []
            for sub_caminho in um_caminho_possivel:
                # [A, B, C]
                print("[gera entrega um estafeta1] Um sub caminho é: ")
                for x in sub_caminho: print("um: ", x.nome)
                for atual in range(0, len(sub_caminho)):
                    # Se for a primeira paragem, tem de sair da base
                    if atual == 0:
                        cam = algoritmo(origem_cidade, sub_caminho[atual])
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append(cam)
                        total_este_caminho += calcula_distancia(cam)
                    else:
                        # Liga as outras duas paragens
                        cam = algoritmo(sub_caminho[atual - 1], sub_caminho[atual])
                        print("Foi analisado o caminho: ")
                        print_caminho(cam)
                        caminhos_pos_algoritmos.append(cam)
                        total_este_caminho += calcula_distancia(cam)

                # Tem de voltar à base
                cam = algoritmo(sub_caminho[atual], origem_cidade)
                print("Foi analisado o caminho: ")
                print_caminho(cam)
                total_este_caminho += calcula_distancia(cam)
                print("Este caminho tem o custo total de: ", total_este_caminho)
                caminhos_pos_algoritmos.append(cam)
            print("<---------Fim de análise de um caminho------->")
            if total_este_caminho < melhor_distancia:
                print("Altera caminho para um melhor, ", total_este_caminho)
                # Guarda as informações do melhor caminho
                melhor_distancia = total_este_caminho
                melhor_caminho.clear()
                melhor_caminho = caminhos_pos_algoritmos.copy()
    # Nenhum caminho é possível, pode ser porque a encomenda é muito pesada
    # Ou duas, ou mais, entregas dum nodo ultrapassa o máximo.
    if melhor_distancia == float(inf):
        print("Nenhuma foi entregue")
    else:
        maximo_possivel = maximo_peso_uma_viagem()
        print("[gera entregas] <---------Tudo gerado-------->")

        for sub_percurso_atual in range(0, len(melhor_caminho) - 1):
            print("<--Entrega-->")
            # Primeiro, vamos ver que encomendas serão entregues nessa viagem
            ids = encomendas_nesse_percurso(melhor_caminho[sub_percurso_atual], encomendas_id)
            pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, ids)
            peso_no_sub_caminho = sum(pesos_no_percurso)
            print("O peso no percurso é: ", peso_no_sub_caminho)
            print("O máximo que podemos transportar é: ", maximo_possivel)
            veiculo = escolhe_veiculo(melhor_caminho[sub_percurso_atual], peso_no_sub_caminho)
            entrega_feita = Entrega(ids, estafeta_id, 0, veiculo, melhor_caminho[sub_percurso_atual])
            entrega_feita.imprime_entrega()

        print("E o caminho de voltar")
        print_caminho(melhor_caminho[len(melhor_caminho)-1])



# Coisas sobre este teste
# Realmente, a mota é mais rápida que o carro, mas não pode levar tanto peso
# Por isso, uma das encomendas tem o peso que dá para a mota, daí a escolher
# Mas a outra pesa muito para a mota, logo é o carro que leva

# Gera todas as atribuições
def gerar_entregas(algoritmo):
    lista_estafetas = {atribuicao.estafeta_id for atribuicao in atribuicoes}

    for estafeta in lista_estafetas:
        gera_entrega_um_estafeta(estafeta, algoritmo)

        print("<------------------>")

