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

  def get_vertices_adjacentes(self, id_vertice):
    vertices_adjacentes = []
    for aresta in self.arestas:
      if aresta.vertice_1 == id_vertice:
        vertices_adjacentes.append(aresta.vertice_2)
      elif aresta.vertice_2 == id_vertice:
        vertices_adjacentes.append(aresta.vertice_1)
    return vertices_adjacentes

  def deleta_vertice(self, id):
    index_remocao = self.get_vertice_index(id)
    self.vertices.pop(index_remocao)
    remover_arestas = self.get_arestas_from_vertice(id)
    for aresta in remover_arestas:
      self.deleta_aresta(aresta)

  def get_arestas_from_vertice(self, id_vertice):
    aux_arestas = []
    for a in self.arestas:
      if a.vertice_1 == id_vertice or a.vertice_2 == id_vertice:
        aux_arestas.append(a.id)
    return aux_arestas
  
  def get_vertice_index(self, id):
    for index, vertice in enumerate(self.vertices):
      if vertice.id == id:
        return index
    else:
      return False

  def get_vertices(self): 
    return self.vertices
  
  def get_arestas(self):
    aux = []
    for aresta in self.arestas:
      aux.append(aresta.vertice_1.nome)
      aux.append(aresta.vertice_2.nome)
      aux.append(aresta.peso)
    return aux