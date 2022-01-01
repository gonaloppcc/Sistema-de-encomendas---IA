from algoritmos_procura.dfs import dfs
from algoritmos_procura.gulosa import resolve_gulosa
from gera_encomendas.geraEntregas import gerar_entregas
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def main():
    algoritmo = resolve_gulosa

    logging.basicConfig(filename='fase2.log', level=logging.INFO)
    logging.debug('Started')

    gerar_entregas(algoritmo)

    logging.debug('Finished')


if __name__ == '__main__':
    main()
