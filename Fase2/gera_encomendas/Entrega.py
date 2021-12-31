import logging

from algoritmos_procura.common import caminho_to_string
from base_conhecimento.baseConhecimento import Transporte


# Entrega
# Regista as seguintes informações:
# ‘Id’ da encomenda, ‘id’ do estafeta, data da entrega, meio utilizado, caminho usado


class Entrega:
    def __init__(self, encomenda_id: int, estafeta_id: int, data_entrega, transporte: Transporte, caminho):
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

    def imprime_entrega(self):
        logging.info(f"Id da encomenda: {self.encomenda_id}")
        logging.info(f"Id da estafeta: {self.estafeta_id}")
        logging.info(f"Data entrega: {self.data_entrega}")
        logging.info(f"Transporte: {self.transporte.nome}")
        logging.info(caminho_to_string(self.caminho))
