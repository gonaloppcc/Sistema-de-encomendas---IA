from algoritmos_procura.dfs import dfs
from algoritmos_procura.gulosa import resolve_gulosa
from gera_encomendas.geraEntregas import gerar_entregas
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def main():
    algoritmo1 = resolve_gulosa
    algoritmo2 = dfs

    logging.basicConfig(filename='fase2.log', level=logging.INFO)
    logging.debug('Começou')

    logging.info(f"Algoritmo da {algoritmo1.__name__}\n")
    gerar_entregas(algoritmo1)

    logging.info(f"Algoritmo da {algoritmo2.__name__}\n")
    gerar_entregas(algoritmo2)

    logging.debug('Acabou')


if __name__ == '__main__':
    main()
