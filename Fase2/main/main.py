import logging

from algoritmos_procura.a_estrela import a_estrela
from algoritmos_procura.gulosa import resolve_gulosa
from gera_encomendas.gera_circuitos import gerar_circuitos

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def main():
    algoritmo1 = a_estrela
    algoritmo2 = resolve_gulosa

    logging.basicConfig(filename='fase2.log', level=logging.INFO)
    logging.debug('Começou')

    logging.info(f"-> Algoritmo da {algoritmo1.__name__}")
    gerar_circuitos(algoritmo1)
    logging.info("")

    logging.info(f"-> Algoritmo da {algoritmo2.__name__}")
    gerar_circuitos(algoritmo2)

    logging.debug('Acabou')


if __name__ == '__main__':
    main()
