# Encomendas Usamos o tipo de dados Data de pyhton, juntando dias e horas encomenda: encomendaID, clienteID, peso,
# volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, localID -> {V,F}.


class Encomenda:
    def __init__(self, encomenda_id: int, cliente_id: int, peso: int, volume: int, prazo: date,
                 data_encomenda: date, id_local_entrega: int):
        """
        Construtor do tipo encomenda.
        @param encomenda_id: Id da encomenda.
        @param cliente_id: Id do cliente.
        @param peso: Peso da encomenda, usado para calcular a velocidade de transporte.
        @param volume: Volume da encomenda.
        @param prazo: Data do prazo.
        @param data_encomenda: Data da encomenda
        @param id_local_entrega: Local onde a encomenda será entregue.
        """
        self.encomenda_id = encomenda_id
        self.cliente_id = cliente_id
        self.peso = peso
        self.volume = volume
        self.prazo = prazo
        self.data_encomenda = data_encomenda
        self.id_local_entrega = id_local_entrega



    def __str__(self):
        return \
            f"""Id={self.encomenda_id}, clienteId={self.cliente_id}, peso={self.peso}, volume={self.volume}, prazo={self.volume}, dataEncomenda={self.data_encomenda}, idLocalEntrega={self.id_local_entrega}
        """

    def cidade_encomenda(self):
        """
        Descobre a cidade de destino de uma encomenda.
        @return: Cidade de destino, na forma de string.
        """
        from base_conhecimento.baseConhecimento import id_locais_cidades
        for cidade, (id_inicio, id_fim) in id_locais_cidades.items():
            if id_inicio <= self.id_local_entrega <= id_fim:
                return cidade
