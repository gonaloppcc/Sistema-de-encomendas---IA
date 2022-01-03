import logging

from algoritmos_procura.dfs import dfs
from gera_encomendas.geraEntregas import gerar_entregas

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def main():
    algoritmo1 = dfs

    logging.basicConfig(filename='fase2.log', level=logging.INFO)
    logging.debug('Começou')

    logging.info(f"-> Algoritmo da {algoritmo1.__name__}")
    gerar_entregas(algoritmo1)
    logging.info("")
    logging.debug('Acabou')


if __name__ == '__main__':
    main()
