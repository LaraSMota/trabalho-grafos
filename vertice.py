class Vertice:
    def __init__(self, id):
        self.id = id
        self.grau = 0
        self.visitado = False
        self.predecessor = []
        self.estimativa = 999999
        self.input = 0
        self.output = 0

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def aumenta_grau(self):
        self.grau += 1

    def diminui_grau(self):
        self.grau -= 1
    
    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado    

    def setImput(self, inp):
        self.input = inp

    def setOutput(self, out):
        self.output = out

    def __str__(self):
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
            self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso