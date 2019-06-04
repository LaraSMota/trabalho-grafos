import xlrd 
from grafo import *

opcao = 0

def imprime_vertices(msg, vertices):
  v_concatenado = ''
  for v in vertices:
    v_concatenado += (v.id + ' ')
  print(msg, v_concatenado, '\n')

def imprime_vertices_adjacentes(msg, vertices):
  v_concatenado = ''
  for v in vertices:
    v_concatenado += (v + ' ')
  print(v_concatenado, '\n')

def imprime_arestas(msg, arestas):
  a_concatenado = ''
  for a in arestas:
    a_concatenado += (a.id + ' ')
  print(msg, a_concatenado, '\n')

def seleciona_funcionalidade(opcao):
  if opcao == 1:  #INSERIR VERTICES
    vertices = input('Digite os vértices: ')
    grafo.criar_vertices(vertices)
  
  elif opcao == 2:  #INSERIR ARESTA
    imprime_vertices('Vértices existentes: ', grafo.vertices)
    aresta_criada = False
    while aresta_criada == False:
      print('OBS: Ambos os vértices devem existir')
      print('------------------------------------')
      id = input('Digite um identificador para a aresta: ').upper()
      vertice_1 = input('Digite o vertice 1: ').upper()
      vertice_2 = input('Digite o vertice 2: ').upper()
      peso = int(input('Digite o peso: '))
      aresta_criada = grafo.criar_aresta(id, vertice_1, vertice_2, peso)
  
  elif opcao == 3:  #DELETAR VERTICE
    imprime_vertices('Vértices criados: ', grafo.vertices)
    id_vertice = input('Digite o id do vértice: ').upper()
    grafo.deleta_vertice(id_vertice)
  
  elif opcao == 4:  #DELETAR ARESTA
    imprime_arestas('Arestas existentes: ', grafo.arestas)
    id_aresta = input('Digite o id da aresta: ').upper()
    aresta_deletada = grafo.deleta_aresta(id_aresta)
    if type(aresta_deletada) == bool and not(aresta_deletada):
      print('A aresta deve ter sido criada para realizar essa ação')
  
  elif opcao == 5: #VERIFICA ARESTA
    v1 = input('Digite o id do primeiro vértice: ').upper()
    v2 = input('Digite o id do segundo vértice: ').upper()
    resposta = grafo.exite_aresta_entre_vertices(v1, v2)
    print('\n', resposta['msg'])
  
  elif opcao == 6: #VERTICES ADJACENTES
    id_vertice = input('Digite o id do vértice: ').upper()
    vertices_adjacentes = grafo.get_vertices_adjacentes(id_vertice)
    imprime_vertices_adjacentes('Vértices adjacentes ao vértice {}:'.format(id_vertice), vertices_adjacentes)
  
  elif opcao == 7:  #IMPRIME GRAU DE VERTICE
    id_vertice = input('Digite o id do vértice: ').upper()
    print('Grau: {}'.format(grafo.get_vertice_grau(id_vertice)))

  elif opcao == 8:  #IMPRIME GRAU MINIMO, MEDIO E MAXIMO
    print("Grau mínimo: {}\n".format(grafo.grau_minimo()))
    print("Grau médio: {}\n".format(grafo.grau_medio()))
    print("Grau máximo: {}".format(grafo.grau_maximo())) 

  elif opcao == 9:
    if grafo.dirigido:
      print('dirigido')
      grafo_conexo = grafo.eh_conexo_dirigido()
    else:
      grafo_conexo = grafo.eh_conexo()
    if grafo_conexo:
      print('Verdadeiro')
    else:
      print('Falso')

  elif opcao == 10: #MATRIZ DE ADJACENCIA
    grafo.imprime_matriz()

  elif opcao == 11: #VERIFICA CAMINHO DE EULER
    euler = grafo.eh_euleriano()
    print(euler)
    if euler:
      print("Existe caminho de euler") 
    else:
      print("Não existe caminho de euler")

  elif opcao == 12: #LE DE ARQUIVO
    grafo.le_arquivo()
    
  elif opcao == 13:  #IMPRIME VERTICES E ARESTAS
    print("Grafo: {}\n".format(grafo.nome))
    imprime_vertices('Vértices existentes: ', grafo.vertices)
    imprime_arestas('Arestas existentes: ', grafo.arestas)
  elif opcao == 14:
    grafo.algoritmo_warshall()
  elif opcao == 15:
    origem = input('Digite o vértice de origem: ').upper()
    grafo.algoritmo_dijkstra(origem)
  elif opcao == 16:
    origem = input('Digite o vértice de origem: ').upper()
    grafo.algoritmo_bellman_ford(origem)
  elif opcao == 17:
    grafo.algoritmo_floyd()
  else:
    print('Xau')

def display_menu():
  print('''
  1 - Inserir vértices
  2 - Inserir aresta
  3 - Remover vértices
  4 - Remover aresta
  5 - Testar existência de aresta entre dois vértices
  6 - Obter os vértices adjacentes a um determinado vértice
  7 - Obter o grau de um determinado vértice
  8 - Obter o grau médio, o grau mínimo e o grau máximo
  9 - Identifique se o grafo é conexo
  10 - Exibir Matriz de Adjacências
  11 - Verificar existência de um caminho de Euler
  12 - Ler entrada a partir de arquivo
  13 - Visualizar vertices e arestas
  14 - Algoritmo de Warshall
  15 - Algoritmo de Dijkstra
  16 - Algoritmo de Bellman-Ford
  17 - Algoritmo de Floyd
  18 - Identificar número de componentes
  19 - Identificar número de vértices no maior componente
  20 - Sair\n''')

print("Seja bem vindo! \n")
nome_grafo = input('Digite nome do grafo: ').upper()
dirigido = input('É dirigido?(s ou n) ').upper()
while dirigido != 'S' and dirigido != 'N':
  dirigido = input('Digite \'s\' ou \'n\': ').upper()
if dirigido == 'S':
  ehdirigido = True
else:
  ehdirigido = False

ponderado = input('É ponderado?(s ou n) ').upper()
while ponderado != 'S' and ponderado != 'N':
  ponderado = input('Digite \'s\' ou \'n\': ').upper()
if ponderado == 'S':
  ehPonderado = True
else:
  ehPonderado = False

global grafo
grafo = Grafo(nome_grafo, ehdirigido, ehPonderado)

while opcao != 20:
  display_menu()
  opcao = int(input('Selecione uma opção: '))
  print('----------------------- \n')
  seleciona_funcionalidade(opcao)