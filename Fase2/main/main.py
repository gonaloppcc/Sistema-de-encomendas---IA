import logging

from algoritmos_procura.bfs import bfs
from algoritmos_procura.dfs_lim import dfs_limited
from base_conhecimento.geraGrafo import gera_grafo
from base_conhecimento.gera_atribuicoes import gera_atribuicoes
from base_conhecimento.gera_encomenda import gera_encomendas
from gera_encomendas.gera_circuitos import gerar_circuitos

"""logging.basicConfig(filename='fase2.log',
                    filemode='w',
                    format='[%(levelname)s] %(asctime)s -  %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
"""
logging.basicConfig(
    format='[%(levelname)s] %(asctime)s -  %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)


def main():
    gera_grafo("Trofa", 30, 5)
    gera_encomendas(2, "Trofa")
    print("Gera encomenda feita")
    gera_atribuicoes()
    print("Gera atribuições feita")

    algoritmo1 = bfs
    algoritmo2 = dfs_limited

    logging.debug('Começou')
    logging.info(f"-> Algoritmo da {algoritmo1.__name__}")
    gerar_circuitos(algoritmo1)
    logging.info("")

    logging.info(f"-> Algoritmo da {algoritmo2.__name__}")
    gerar_circuitos(algoritmo2)
    print("Gera circuitos feita")

    logging.debug('Acabou')


if __name__ == '__main__':
    main()
