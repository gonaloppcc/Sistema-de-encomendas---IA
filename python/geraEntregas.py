#Entrega 
#Regista as seguintes informações:
# Id da encomenda, id do estafeta, data da entrega, meio utilizado, caminho usado 
class Entrega:
    def __init__(self, encomenda_id, estafeta_id, data_entrega, transporte, caminho):
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id 
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

entregas_feitas = []