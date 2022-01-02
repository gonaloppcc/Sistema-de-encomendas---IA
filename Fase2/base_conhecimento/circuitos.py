from base_conhecimento import baseConhecimento


# TODO: Criar um dicionário para armazenar as entregas de um percurso

# Gerar entregas
"""
1. Procuramos atribuições
2. Por cada atribuição vamos buscar o destino da encomenda
3. Estafeta + destino da encomenda = caminho
4. Guardar caminho, com ‘id’ da encomenda
5. Entrega = informações + caminho. Ao decidir o veículo usado na entrega,
vemos uma flag que diz se queremos ser rápidos ou ecológicos.
Adicionar aos circuitos efetuados, e criar ‘id’ da entrega.

 circuito : (counter, peso, volume, entregas)
 circuito -> String do circuito
 counter  -> Nº de vezes que o percurso foi feito
 peso     -> Peso total de todas as entregas feitas neste percurso
 volume   -> Volume total de todas as entregas feitas neste percurso
 entregas -> Lista de listas de entregas
"""
circuitosEfetuados = {

}


# Retorna uma lista ordenada pelo seu fator
# de produtividade, (nº de entregas / nº de percursos).
# Esta lista está ordenada por ordem descendente, ou seja,
# os circuitos com um valor de produtividade mais elevado
# aparecem primeiro.
def circuitos_mais_produtivos():
    lista = []
    for (circuito, info) in circuitosEfetuados.items():
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
    return max(circuitosEfetuados.items(), key=lambda circuito: circuito[1][0])


# Calcula o circuito mais usado com base no
# peso total das entregas do percurso.
def circuito_mais_usado_peso():
    return max(circuitosEfetuados.items(), key=lambda x: x[1][1])


# Calcula o circuito mais usado com base no
# volume total das entregas do percurso
def circuito_mais_usado_volume():
    return max(circuitosEfetuados.items(), key=lambda x: x[1][2])


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

    if circuito not in circuitosEfetuados:
        circuitosEfetuados[circuito] = (1, peso, volume, [entregas])
    else:
        nova_l = circuitosEfetuados[circuito][3]
        nova_l.append(entregas)

        inc = circuitosEfetuados[circuito][0] + 1
        novo_peso = circuitosEfetuados[circuito][1] + peso
        novo_vol = circuitosEfetuados[circuito][2] + volume

        circuitosEfetuados[circuito] = (inc, novo_peso, novo_vol, nova_l)
