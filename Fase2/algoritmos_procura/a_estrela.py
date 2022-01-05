import logging

from algoritmos_procura.common import calcula_norma, conectados, arestas


def heuristica(nodo1, nodo2):
    return calcula_norma(nodo1, nodo2)


def a_estrela(origem, destino):
    logging.debug(f"Origem: {origem}")

    aberto = []  # Nodos ainda não passados
    fechado = []  # Nodos já passados
    aberto.append(origem)

    distancias = {}  # Distancia + curta até ao nodo
    pais = {}

    distancias[origem] = 0
    pais[origem] = origem

    while len(aberto) > 0:
        logging.debug("Passou no while")
        n = None  # Nodo com o menor f
        for nodo in aberto:
            if n is None or distancias[nodo] + heuristica(nodo, destino):
                n = nodo
        logging.debug(f"Nodo escolhido: {n}")

        if n == destino or conectados(n) == []:
            logging.debug("n == destino or conectados(n) == [] Verdade")
            pass
        else:
            for (nodo, peso) in arestas(n):
                logging.debug(f"(nodo, peso) -> ({nodo}, {peso})")
                if nodo not in aberto and nodo not in fechado:
                    aberto.append(nodo)
                    pais[nodo] = n
                    distancias[nodo] = distancias[n] + peso
                else:
                    if distancias[nodo] > distancias[n] + peso:
                        # Distancia do nodo encontrada é menor que a distância antiga do nodo.
                        distancias[nodo] = distancias[n] + peso
                        pais[nodo] = n
        if n is None:
            logging.info('Caminho não existe!')
            return None
        elif n == destino:
            caminho = []

            while pais[n] != n:
                caminho.append(n)
                n = pais[n]

            caminho.append(origem)
            caminho.reverse()

            logging.debug("Caminho: {}".format(caminho))
            return caminho

        logging.debug("Nodo removido do aberto e adicionado ao fechado")
        aberto.remove(n)
        fechado.append(n)

    logging.info("Não existe o caminho!")
    return None
