from algoritmos_procura.common import print_caminho
from base_conhecimento.baseConhecimento import Transporte


# Entrega
# Regista as seguintes informações:
# ‘Id’ da encomenda, ‘id’ do estafeta, data da entrega, meio utilizado, caminho usado


class Entrega:
    def __init__(self, encomenda_id, estafeta_id: int, data_entrega, transporte: Transporte, caminho):
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

    def imprime_entrega(self):
        print("Id da encomenda: ", self.encomenda_id)
        print("Id da estafeta: ", self.estafeta_id)
        print("Data entrega: ", self.data_entrega)
        print("Transporte: ", self.transporte.nome)
        print("Caminho feito: ")
        print_caminho(self.caminho)

