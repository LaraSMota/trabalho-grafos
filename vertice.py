class Vertice:
    def __init__(self, id):
        self.id = id
        self.grau = 0

    def aumenta_grau(self):
        self.grau += 1

    def diminui_grau(self):
        self.grau -= 1