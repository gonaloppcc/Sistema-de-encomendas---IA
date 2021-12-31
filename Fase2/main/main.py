from gera_encomendas.geraEntregas import gerar_entregas
import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.basicConfig(filename='fase2.log', level=logging.INFO)
    logging.info('Started')

    gerar_entregas()

    logging.info('Finished')


if __name__ == '__main__':
    main()
