class Vertice:
    def __init__(self, id):
        self.id = id
        self.grau = 0
        self.visitado = False
        self.predecessor = []
        self.estimativa = 999999

    def aumenta_grau(self):
        self.grau += 1

    def diminui_grau(self):
        self.grau -= 1
    
    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa