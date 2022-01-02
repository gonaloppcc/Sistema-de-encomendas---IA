# Encomendas Usamos o tipo de dados Data de pyhton, juntando dias e horas encomenda: encomendaID, clienteID, peso,
# volume, prazoEntrega, horasPrazoEntrega, dataDeEncomenda, horasDataEncomenda, localID -> {V,F}.
class Encomenda:
    def __init__(self, encomenda_id, cliente_id, peso, volume, prazo, data_encomenda, id_local_entrega):
        self.encomenda_id = encomenda_id
        self.cliente_id = cliente_id
        self.peso = peso
        self.volume = volume
        self.prazo = prazo
        self.data_encomenda = data_encomenda
        self.id_local_entrega = id_local_entrega
