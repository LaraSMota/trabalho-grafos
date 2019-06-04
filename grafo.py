from vertice import *
from aresta import *
import xlrd
import math

class Grafo:

  aux_arestas = []
  arestas_indices = {}
  matriz = []

  def __init__(self, nome, dirigido, ponderado):
    self.nome = nome
    self.dirigido = dirigido
    self.ponderado = ponderado
    self.vertices = []
    self.arestas = []
    self.visitado = []

  def criar_aresta(self, id, vertice_1, vertice_2, peso):
    existe_vertice_1 = self.elemento_existe(vertice_1, self.vertices)
    existe_vertice_2 = self.elemento_existe(vertice_2, self.vertices)
    if existe_vertice_1 and existe_vertice_2:
      self.aumenta_grau_vertice(vertice_1)
      self.aumenta_grau_vertice(vertice_2)
      aresta = Aresta(id.upper(), vertice_1, vertice_2, peso)
      self.arestas.append(aresta)
      return True
    else:
      return False

  def aumenta_grau_vertice(self, id_vertice):
    index = self.get_vertice_index(id_vertice)
    self.vertices[index].aumenta_grau()
  
  def diminui_grau_vertice(self, id_vertice):
    index = self.get_vertice_index(id_vertice)
    self.vertices[index].diminui_grau()

  def criar_vertices(self, id):
    lista_vertices = self.get_lista_elementos(id)
    for v in lista_vertices:
      if self.elemento_existe(v, self.vertices):
        print("Vertice {} já existe na lista".format(v))
      else:
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
    aresta = self.arestas.pop(index)
    vertice_1 = aresta.vertice_1
    vertice_2 = aresta.vertice_2
    self.diminui_grau_vertice(vertice_1)
    self.diminui_grau_vertice(vertice_2)
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

  def get_vertices_adjacentes_dirigido(self, id_vertice):
    vertices_adjacentes = []
    for aresta in self.arestas:
      if aresta.vertice_1 == id_vertice:
        vertices_adjacentes.append(aresta.vertice_2)
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

  def grau_minimo(self):
    graus_vertices = self.lista_graus()
    return min(graus_vertices)

  def grau_medio(self):
    graus_vertices = self.lista_graus()
    return sum(graus_vertices)/len(graus_vertices)
    
  def grau_maximo(self):
    graus_vertices = self.lista_graus()
    return max(graus_vertices)
  
  def lista_graus(self):
    aux = []
    for vertice in self.vertices:
      aux.append(vertice.grau)
    return aux

  def get_vertice_grau(self, id):
    index = self.get_vertice_index(id.upper())
    vertice = self.vertices[index]
    return vertice.grau

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

  def exite_aresta_entre_vertices(self, v1, v2):
    resposta = {"msg": "Não existe aresta entre os vértices {} e {}.".format(v1, v2)}
    v1_existe = self.elemento_existe(v1, self.vertices)
    v2_existe = self.elemento_existe(v2, self.vertices)
    if v1_existe and v2_existe:
      for aresta in self.arestas:
        if (aresta.vertice_1 == v1 and aresta.vertice_2 == v2) or (aresta.vertice_1 == v2 and aresta.vertice_2 == v1):
          resposta = {"msg": "Existe uma aresta entre os vértices {} e {}.".format(v1, v2)}
          return resposta
    else:
      resposta = {"msg": "Ambos os vértices devem existir."}
    return resposta

  def le_arquivo(self):
    arquivo = xlrd.open_workbook("grafo.xlsx")

    planilha_vertices = arquivo.sheet_by_index(0)
    dado_coluna = planilha_vertices.col(0)
    for texto in dado_coluna:
      self.criar_vertices(texto.value)

    planilha_arestas = arquivo.sheet_by_index(1)
    tam = planilha_arestas.nrows
    while tam > 0:
      self.criar_aresta(planilha_arestas.cell_value(tam-1, 0), planilha_arestas.cell_value(tam-1, 1), planilha_arestas.cell_value(tam-1, 2), planilha_arestas.cell_value(tam-1, 3))
      tam -= 1
  def eh_conexo(self):
    self.visitado = []
    vertices_visitados = self.busca_em_profundidade(self.vertices[0].id)
    return len(vertices_visitados) == len(self.vertices)

  def eh_conexo_dirigido(self):
    self.visitado = []
    vertices_visitados = self.busca_em_profundidade_dirigido(self.vertices[0].id)
    return len(vertices_visitados) == len(self.vertices)

  def busca_em_profundidade(self, id):
    self.visitado.append(id)
    v_adjacentes = self.get_vertices_adjacentes(id)
    for v in v_adjacentes:
      if not(v in self.visitado):
        self.busca_em_profundidade(v)
    return self.visitado
  
  def busca_em_profundidade_dirigido(self, id):
    self.visitado.append(id)
    v_adjacentes = self.get_vertices_adjacentes_dirigido(id)
    for v in v_adjacentes:
      if not(v in self.visitado):
        self.busca_em_profundidade_dirigido(v)
    return self.visitado

  def eh_euleriano(self):
    resposta = self.eh_conexo()
    impares = 0
    if (resposta):
      for i in self.vertices:
        if (i.grau % 2 != 0):
          impares += 1
      if (impares == 0) or (impares == 2):
        result = True
      else: 
        result = False
    else:
      result = False
    return result
  
  def gera_matriz_de_adjacencia(self):
    self.aux_arestas = []
    self.matriz = []
    self.arestas_indices = {}
    if self.ponderado and not(self.dirigido):
      self.gera_matriz_caminho_minimo()
    else:
      self.gera_matriz_com_zeros()
    for aresta in self.arestas:
      self.aux_arestas.append(aresta.id + str(aresta.peso))
    if self.ponderado and not(self.dirigido):
      for a in self.aux_arestas:
        if len(a) == 6:
          peso = a[2:4]
        else:
          peso = a[2:3]
        self.matriz_adjacencia_ponderada(a[:1], a[1:2], peso)
    elif self.ponderado and self.dirigido:
      for a in self.aux_arestas:
        self.matriz_adjacencia_ponderada_dirigida(a[:1], a[1:2], a[2:3])
    elif not(self.ponderado) and not(self.dirigido):
      for a in self.aux_arestas:
        self.matriz_adjacencia(a[:1], a[1:2])
    elif not(self.ponderado) and self.dirigido:
      for a in self.aux_arestas:
        self.matriz_adjacencia_dirigida(a[:1], a[1:2])

    # DEIXA MATRIZ BONITINHA PRA SER IMPRESSA :)
    # matriz_aux = []
    # linha_aux = []
    # linha_aux.append(" ")
    # for vertice in self.vertices:
    #   linha_aux.append(vertice.id)
    # matriz_aux.append(linha_aux)
    # aux = 0
    # for vertice in self.vertices:
    #   linha_aux = []
    #   linha_aux.append(vertice.id)
    #   for registro in self.matriz[aux]:
    #     linha_aux.append(registro)
    #   matriz_aux.append(linha_aux)
    #   aux += 1
    # self.matriz = matriz_aux
    return self.matriz

  def gera_matriz_caminho_minimo(self):
    INF = 99999
    for vertice in self.vertices:
      self.matriz.append([INF] * (len(self.vertices)))
      self.arestas_indices[vertice.id] = len(self.arestas_indices)
    self.adiciona_zero_a_diagonal() 

  def gera_matriz_com_zeros(self):
    for vertice in self.vertices:
      self.matriz.append([0] * (len(self.vertices)))
      self.arestas_indices[vertice.id] = len(self.arestas_indices)

  def gera_copia_matriz_com_zeros(self):
    matriz_copia = []
    for vertice in self.vertices:
      matriz_copia.append([0] * (len(self.vertices)))
    return matriz_copia

  def adiciona_zero_a_diagonal(self):
    for i in range(len(self.vertices)):
      self.matriz[i][i] = 0


  def matriz_adjacencia_ponderada(self, v1, v2, peso):
    self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]] = int(peso)    
    self.matriz[self.arestas_indices[v2]][self.arestas_indices[v1]] = int(peso) 
  
  def matriz_adjacencia(self, v1, v2):
    self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]] = int(self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]]) + 1  
    self.matriz[self.arestas_indices[v2]][self.arestas_indices[v1]] = int(self.matriz[self.arestas_indices[v2]][self.arestas_indices[v1]]) + 1
  
  def matriz_adjacencia_dirigida(self, v1, v2):
    self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]] = int(self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]]) + 1

  def matriz_adjacencia_ponderada_dirigida(self, v1, v2, peso):
    self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]] = int(self.matriz[self.arestas_indices[v1]][self.arestas_indices[v2]]) + int(peso)

  def imprime_matriz(self):
    matriz = self.gera_matriz_de_adjacencia()
    tam = len(self.vertices) + 1
    for linha in range(len(self.vertices)):
      print("{}\n".format(matriz[linha]))
  
  def algoritmo_warshall(self):
    self.gera_matriz_de_adjacencia()
    for k in range(len(self.vertices)):
      for i in range(len(self.vertices)):
        for j in range(len(self.vertices)):
          self.matriz[i][j] = self.matriz[i][j] or (self.matriz[i][k] and self.matriz[k][j])
    self.imprime_matriz_acessibilidade()
  
  def imprime_matriz_acessibilidade(self):
    for linha in range(len(self.vertices)):
      print("{}\n".format(self.matriz[linha]))

  def algoritmo_floyd(self):
    caminho = self.gera_copia_matriz_com_zeros()
    for k in range(len(self.vertices)): 
      for i in range(len(self.vertices)):
        for j in range(len(self.vertices)):
          if self.matriz[i][k] + self.matriz[k][j] < self.matriz[i][j]:
            self.matriz[i][j] = self.matriz[i][k] + self.matriz[k][j]
            caminho[i][j] = k
    self.imprime_matriz()
    self.imprime_matriz_caminho(caminho)

  def imprime_matriz_caminho(self, matriz):
    for linha in range(len(self.vertices)):
      print("{}\n".format(matriz[linha]))
  
  def algoritmo_bellman_ford(self, start):
    dist = []
    for i in range(len(self.vertices)):
      dist.append(99999)
    dist[self.get_vertice_index(start)] = 0

    relaxedAnEdge = True

    for v in range(len(self.vertices)):
      if relaxedAnEdge:
        relaxedAnEdge = False
        for edge in self.arestas:
          if dist[self.get_vertice_index(edge.vertice_1)] + edge.peso < dist[self.get_vertice_index(edge.vertice_2)]:
            dist[self.get_vertice_index(edge.vertice_2)] = dist[self.get_vertice_index(edge.vertice_1)] + edge.peso
            relaxedAnEdge = True
    print(dist)
  
  def algoritmo_dijkstra(self, origem):
        fonte = self.busca_Vertice(origem)
        if fonte is None:
          print("Vertice Nulo")
          return

        self.inicializa_Fonte(fonte)
        tempo = 0
        lista = []
        resposta = []  # conjunto resposta
        lista_vertices = []
        for i in lista_vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.get_vertices_adjacentes(u)
            if v is None:
              for i in lista_vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                i.setVisitado(False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
              tempo += 1
              u.setImput(tempo)  # apenas mostra a ordem de visitação do grafo
              resposta.append(lista[0])
              lista.pop(0)  # retiro vertice sem adjacente da lista

            else:
              w = self.exite_aresta_entre_vertices(u, v)
              if w is not None:
                self.relaxa_Vertice(u, v, w)

        print("Estimativas: ")
        for i in resposta:
          print(i)  # imprimo as respostas
    
  
  def inicializa_Fonte(self, fonte):  # Função usado no BFS e Dijkstra Método recebe um Objeto
      lista_vertices = []
      for v in lista_vertices:
        v.setEstimativa(99999)
        v.setVisitado(False)
      fonte.setVisitado(True)
      fonte.setEstimativa(0)

  def relaxa_Vertice(self, u, v, w):
    if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
      v.setEstimativa(u.getEstimativa() + w.getPeso())
      v.predecessor.append(u.getId())  # guarda apenas o id
  
  def busca_Vertice(self, identificador):  # Método recebe um int
    lista_vertices = self.vertices
    for i in lista_vertices:
      if identificador.upper() == i.id.upper():
        return i
    return None