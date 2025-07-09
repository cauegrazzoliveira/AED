from Torre import Torre
class Apartamento:
    def __init__(self, torre = Torre):
        self.id = 1
        self.numero = "101"
        self.torre = torre
        self.vaga = None
        self.prox = None
        self.fim = None