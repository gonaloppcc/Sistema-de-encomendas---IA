# Encomendas Usamos o tipo de dados Data de pyhton, juntando dias e horas encomenda: encomendaID, clienteID, peso,
# volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, localID -> {V,F}.


class Encomenda:
    def __init__(self, encomenda_id: int, cliente_id: int, peso: int, volume: int, prazo: object,
                 data_encomenda: object, id_local_entrega: id):
        """
        Construtor do tipo encomenda.
        @param encomenda_id: Id da encomenda.
        @param cliente_id: Id do cliente.
        @param peso: Peso da encomenda, usado para calcular a velocidade de transporte.
        @param volume: Volume da encomenda.
        @param prazo:
        @param data_encomenda:
        @param id_local_entrega: Local onde a encomenda será entregue.
        """
        self.encomenda_id = encomenda_id
        self.cliente_id = cliente_id
        self.peso = peso
        self.volume = volume
        self.prazo = prazo
        self.data_encomenda = data_encomenda
        self.id_local_entrega = id_local_entrega
