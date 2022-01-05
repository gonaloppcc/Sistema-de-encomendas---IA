import logging

from algoritmos_procura.a_estrela import a_estrela
from algoritmos_procura.dfs import dfs
from algoritmos_procura.gulosa import resolve_gulosa
from base_conhecimento.geraGrafo import gera_grafo
from gera_encomendas.geraEntregas import gerar_entregas

logging.basicConfig(filename='fase2.log',
                    filemode='w',
                    format='[%(levelname)s] %(asctime)s -  %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def main():
    gera_grafo("Trofa", 30, 5)
    algoritmo1 = a_estrela
    algoritmo2 = resolve_gulosa

    # logging.debug('Começou')
    # logging.info(f"-> Algoritmo da {algoritmo1.__name__}")
    # gerar_entregas(algoritmo1)
    # logging.info("")

    logging.info(f"-> Algoritmo da {algoritmo2.__name__}")
    gerar_entregas(algoritmo2)

    logging.debug('Acabou')


if __name__ == '__main__':
    main()
