import logging
# Gerar entregas
from datetime import timedelta

from algoritmos_procura.common import calcula_distancia, calcula_tempo_transporte
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import entregas, circuitos_efetuados, encomendas
from gera_encomendas.Entrega import Entrega
from gera_encomendas.gera_veiculos import escolhe_veiculo


# Retorna uma lista ordenada pelo seu fator
# de produtividade, (nº de entregas / nº de percursos).
# Esta lista está ordenada por ordem descendente, ou seja,
# os circuitos com um valor de produtividade mais elevado
# aparecem primeiro.
def circuitos_mais_produtivos():
    lista = []
    for (circuito, info) in circuitos_efetuados.items():
        n_entregas = 0
        for entrega in info[3]:
            n_entregas += len(entrega)
        produtividade = n_entregas / info[0]
        lista.append((circuito, produtividade))
    lista.sort(reverse=True, key=lambda x: x[1])
    return lista


# Calcula o circuito mais usado com base no
# número de vezes que foi percorrido
def circuito_mais_usado_counter():
    circ_maior_counter = max(circuitos_efetuados.items(), key=lambda circuito: circuito[1][0])
    return circ_maior_counter[0], circ_maior_counter[1][0]


# Calcula o circuito mais usado com base no
# peso total das entregas do percurso.
def circuito_mais_usado_peso():
    circ_maior_peso = max(circuitos_efetuados.items(), key=lambda x: x[1][1])
    return circ_maior_peso[0], circ_maior_peso[1][1]


# Calcula o circuito mais usado com base no
# volume total das entregas do percurso
def circuito_mais_usado_volume():
    circ_maior_vol = max(circuitos_efetuados.items(), key=lambda x: x[1][2])
    return circ_maior_vol[0], circ_maior_vol[1][2]


# Adicionar circuitos à lista de circuitos
# Esta função adiciona um novo elemento ao dicionário
# de entregas. Caso o circuito não exista, criamos uma nova entrada.
# Caso contrário, damos append das entregas à lista de entregas e incrementamos
# o counter de entregas.
def add_circuito_aux(circuito, entregas):
    peso = 0
    volume = 0
    for encomenda in entregas:
        peso += encomendas[encomenda].peso
        volume += encomendas[encomenda].volume

    if circuito not in circuitos_efetuados:
        circuitos_efetuados[circuito] = (1, peso, volume, [entregas.copy()])
    else:
        nova_l = circuitos_efetuados[circuito][3]
        nova_l.append(entregas.copy())

        inc = circuitos_efetuados[circuito][0] + 1
        novo_peso = circuitos_efetuados[circuito][1] + peso
        novo_vol = circuitos_efetuados[circuito][2] + volume

        circuitos_efetuados[circuito] = (inc, novo_peso, novo_vol, nova_l)


def adiciona_circuito(caminhos: [Local], encomendas_entregues: [int], estafeta_id: int):
    """
    Função que adiciona um circuito aos circuitos_efetuados.
    Os caminhos recebidos começam e acabam na origem duma cidade, logo são circuitos de entrega.
    Aqui tratamos de converter essas informações para entregas, e guarda-las corretamente
    @param caminhos: Conjunto de paragens pertencentes a um circuito
    @param encomendas_entregues: Id's das encomendas entregues nesse circuito.
    @param estafeta_id: Estafeta que realizou o circuito.
    """
    logging.info("<-- Gera um circuito novo --> ")
    # Gerar entrega
    veiculo_escolhido = escolhe_veiculo((caminhos, encomendas_entregues))

    # Tamanho do caminho
    tamanho_do_caminho = calcula_distancia(caminhos)
    for encomenda_id in encomendas_entregues:
        # Calcular tempo de entrega
        pesos_no_percurso = map(lambda id_encomenda: encomendas.get(id_encomenda).peso, encomendas_entregues)
        peso_total = sum(pesos_no_percurso)
        data_entrega = calcula_data_entrega(caminhos, encomenda_id, peso_total, veiculo_escolhido)
        entregas.append(Entrega(encomenda_id, estafeta_id, data_entrega, veiculo_escolhido, caminhos.copy()))
    # Gerar circuito
    # Formar a key para inserir no circuitos_gerados.
    caminhos_juntos = ""
    ultima_passagem = None
    for caminho in caminhos:
        # É importante não repetir elementos repetidos seguidos, isto acontece porque quando duas encomendas são
        # entregues no mesmo sítio, o circuito é o mesmo, mas para duas vezes para entregar.
        if caminho != ultima_passagem:
            caminhos_juntos += caminho.nome + ";"
            ultima_passagem = caminho
    for encomenda in encomendas_entregues:
        logging.info(f"Encomenda entregue: {encomenda}")
        logging.info(f"Peso da encomenda: {encomendas.get(encomenda).peso}")
    logging.info(f"Key do circuito: {caminhos_juntos}")
    logging.info(f"Custo do circuito: {tamanho_do_caminho}")
    logging.info(f"Veículo utilizado: {veiculo_escolhido.nome}")

    logging.info(" ")

    add_circuito_aux(caminhos_juntos, encomendas_entregues)


def calcula_data_entrega(caminho, encomenda_id, peso_total, veiculo_escolhido):
    """
    Calcula a data de entrega de uma encomenda, a partir das suas caraterísticas,
    @param caminho: Caminho realizado para entregar a encomenda.
    @param encomenda_id: Id da encomenda.
    @param peso_total: Peso das encomendas entregues nesse caminho.
        Para calcular a velocidade de transporte, e consequentemente o tempo de entrega,
    @param veiculo_escolhido: Veículo usado para realizar a entrega.
        Necessário para saber a velocidade da entrega, e consequentemente o tempo.
    @return: Tempo da entrega, mas no dia seguinte.
    """

    distancia_caminho = calcula_distancia(caminho)
    duracao_transporte = calcula_tempo_transporte(veiculo_escolhido, peso_total, distancia_caminho)
    data_encomenda = encomendas.get(encomenda_id).data_encomenda
    data_entrega = data_encomenda + timedelta(days=duracao_transporte * 0.4 + 1)

    logging.info(f"Data de encomenda:  {encomendas.get(encomenda_id).data_encomenda.strftime('%d %b %Y')}")
    logging.info(f"Data de entrega: {data_entrega.strftime('%d %b %Y')}")

    return data_entrega


"""
# Retorna uma lista ordenada pelo seu fator
# de produtividade, (nº de entregas / nº de percursos).
# Esta lista está ordenada por ordem descendente, ou seja,
# os circuitos com um valor de produtividade mais elevado
# aparecem primeiro.
def circuitos_mais_produtivos():
    lista = []
    for (circuito, info) in circuitos_efetuados.items():
        n_entregas = 0
        for entrega in info[3]:
            n_entregas += len(entrega)
        produtividade = n_entregas / info[0]
        lista.append((circuito, produtividade))
    lista.sort(reverse=True, key=lambda x: x[1])
    return lista


# Calcula o circuito mais usado com base no
# número de vezes que foi percorrido
def circuito_mais_usado_counter():
    return max(circuitos_efetuados.items(), key=lambda circuito: circuito[1][0])


# Calcula o circuito mais usado com base no
# peso total das entregas do percurso.
def circuito_mais_usado_peso():
    return max(circuitos_efetuados.items(), key=lambda x: x[1][1])


# Calcula o circuito mais usado com base no
# volume total das entregas do percurso
def circuito_mais_usado_volume():
    return max(circuitos_efetuados.items(), key=lambda x: x[1][2])


# Adicionar circuitos à lista de circuitos
# Esta função adiciona um novo elemento ao dicionário
# de entregas. Caso o circuito não exista, criamos uma nova entrada.
# Caso contrário, damos append das entregas à lista de entregas e incrementamos
# o counter de entregas.
def add_circuito(circuito, entregas):
    peso = 0
    volume = 0
    for encomenda in entregas:
        peso += baseConhecimento.encomendas[encomenda].peso
        volume += baseConhecimento.encomendas[encomenda].volume

    if circuito not in circuitos_efetuados:
        circuitos_efetuados[circuito] = (1, peso, volume, [entregas])
    else:
        nova_l = circuitos_efetuados[circuito][3]
        nova_l.append(entregas)

        inc = circuitos_efetuados[circuito][0] + 1
        novo_peso = circuitos_efetuados[circuito][1] + peso
        novo_vol = circuitos_efetuados[circuito][2] + volume

        circuitos_efetuados[circuito] = (inc, novo_peso, novo_vol, nova_l)
=======
>>>>>>> geraGrafo
"""
