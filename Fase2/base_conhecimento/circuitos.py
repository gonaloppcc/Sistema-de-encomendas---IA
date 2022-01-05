import logging

# Gerar entregas
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
def add_circuito_aux(circuito, entregas):
    peso = 0
    volume = 0
    for encomenda in entregas:
        peso += encomendas[encomenda].peso
        volume += encomendas[encomenda].volume

    if circuito not in circuitos_efetuados:
        circuitos_efetuados[circuito] = (1, peso, volume, [entregas])
    else:
        nova_l = circuitos_efetuados[circuito][3]
        nova_l.append(entregas)

        inc = circuitos_efetuados[circuito][0] + 1
        novo_peso = circuitos_efetuados[circuito][1] + peso
        novo_vol = circuitos_efetuados[circuito][2] + volume

        circuitos_efetuados[circuito] = (inc, novo_peso, novo_vol, nova_l)


def adiciona_circuito(caminhos: [Local], encomendas_entregues: [int], estafeta_id: int):
    """
    Função que adiciona um circuito aos circuitos_efetuados.
    Os caminhos recebidos começam e acabam na origem duma cidade, logo são circuitos de entrega.
    Aqui tratamos de converter essas informações para entregas, e guardá-las corretamente
    @param caminhos: Conjunto de paragens pertencentes a um circuito
    @param encomendas_entregues: Id's das encomendas entregues nesse circuito.
    @param estafeta_id: Estafeta que realizou o circuito.
    """
    logging.info("<-- Gera um circuito novo --> ")
    # Gerar entrega
    veiculo_escolhido = escolhe_veiculo((caminhos, encomendas_entregues))
    for encomenda_id in encomendas_entregues:
        entregas.append(Entrega(encomenda_id, estafeta_id, 0, veiculo_escolhido, caminhos.copy()))

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
    logging.info(f"Key do circuito: {caminhos_juntos}")
    logging.info(f"Veículo utilizado: {veiculo_escolhido.nome}")

    logging.info(" ")

    add_circuito_aux(caminhos_juntos, encomendas_entregues)
