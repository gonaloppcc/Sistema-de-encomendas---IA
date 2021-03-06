from datetime import datetime

from algoritmos_procura.common import caminho_to_string
from base_conhecimento.baseConhecimento import Transporte, encomendas
from base_conhecimento.baseConhecimento import entregas
from base_conhecimento.entidades.Estafeta import Estafeta
from base_conhecimento.entidades.Local import Local


# Entrega
# Regista as seguintes informações:
# ‘Id’ da encomenda, ‘id’ do estafeta, data da entrega, meio utilizado, caminho usado


#

class Entrega:
    def __init__(self, encomenda_id: int, estafeta_id: int, data_entrega: datetime, transporte: Transporte,
                 caminho: [Local]):
        """
        Construtor duma entrega. É chamado ao mesmo tempo que os circuitos são gerados, para saber quais os caminhos de
        entrega.
        @param encomenda_id: Id da encomenda
        @param estafeta_id: Id do estafeta que entregou.
        @param data_entrega: Data da encomenda mais a de transporte.
        @param transporte: Veículo utilizado durante a entrega.
        @param caminho: Caminho utilizado durante para a entrega.
        """
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

    def __str__(self):
        """
        Função utilizada para imprimir uma entrega de forma organizada.
        """
        descricao = ""
        descricao += f"\nId da encomenda:  {self.encomenda_id}\n"
        descricao += f"Estafeta: {Estafeta.get_nome_estafeta(self.estafeta_id)}\n"
        descricao += f"Data entrega: {self.data_entrega}\n"
        descricao += f"Transporte: {self.transporte.nome}\n"
        descricao += f"Peso: {encomendas.get(self.encomenda_id).peso}\n"
        descricao += caminho_to_string(self.caminho)
        return descricao

    @staticmethod
    def encomenda_entregue(encomenda_id: int) -> bool:
        """
        Função que verifica se uma encomenda já foi entregue, pelo seu id,
        @return: se a encomenda já foi entregue.
        """
        for entrega in entregas:
            if entrega.encomenda_id == encomenda_id:
                return True
        return False
