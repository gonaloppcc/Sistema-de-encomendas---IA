import logging

from algoritmos_procura.a_estrela import a_estrela
from algoritmos_procura.bfs import bfs
from algoritmos_procura.gulosa import resolve_gulosa
from base_conhecimento.gera_atribuicoes import gera_atribuicoes
from base_conhecimento.gera_encomenda import gera_encomendas
from gera_encomendas.gera_circuitos import gerar_circuitos
from base_conhecimento.geraGrafo import gera_grafo

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
    print("Gera atribuicoes feita")

    algoritmo1 = bfs
    algoritmo2 = bfs

    # logging.debug('Começou')
    # logging.info(f"-> Algoritmo da {algoritmo1.__name__}")
    # gerar_circuitos(algoritmo1)
    # logging.info("")

    logging.info(f"-> Algoritmo da {algoritmo2.__name__}")
    gerar_circuitos(algoritmo2)
    print("Gera cicruitos feita")



    logging.debug('Acabou')


if __name__ == '__main__':
    main()
