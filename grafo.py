from vertice import *
from aresta import *

class Grafo:

  identificador = 0

  def __init__(self, nome, direcionado):
    self.nome = nome
    self.direcionado = direcionado
    self.vertices = []
    self.arestas = []

  def criar_aresta(self, id, vertice_1, vertice_2, peso):
    existe_vertice_1 = self.elemento_existe(vertice_1, self.vertices)
    existe_vertice_2 = self.elemento_existe(vertice_2, self.vertices)
    if existe_vertice_1 and existe_vertice_2:
      aresta = Aresta(id, vertice_1, vertice_2, peso)
      self.arestas.append(aresta)
      return True
    else:
      return False

  def criar_vertices(self, id):
    lista_vertices = self.get_lista_elementos(id)
    for v in lista_vertices:
      vertice = Vertice(v.upper())
      self.vertices.append(vertice)
    return self.vertices
  
  def get_lista_elementos(self, id):
    return id.split(' ')
    
  def elemento_existe(self, elemento, array):
    for v in array:
      if v.id == elemento.upper():
        return True
    return False

  def deleta_aresta(self, id):
    index = self.get_aresta_index(id)
    self.arestas.pop(index)
    return index

  def get_aresta_index(self, id_aresta):
    for index, aresta in enumerate(self.arestas):
      if aresta.id == id_aresta:
        return index
    else:
      return False


  def deleta_vertice(self, id):
    index_remocao = self.get_vertice_index(id)
    self.vertices.pop(index_remocao)
  
  def get_vertice_index(self, nome):
    for index, vertice in enumerate(self.vertices):
      if vertice.id == id:
        return index

  def get_vertices(self): 
    return self.vertices
  
  def get_arestas(self):
    aux = []
    for aresta in self.arestas:
      aux.append(aresta.vertice_1.nome)
      aux.append(aresta.vertice_2.nome)
      aux.append(aresta.peso)
    return aux