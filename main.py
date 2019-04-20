from grafo import *

opcao = 0

def imprime_vertices(msg, vertices):
  v_concatenado = ''
  for v in vertices:
    v_concatenado += (v.id + ' ')
  print(msg, v_concatenado, '\n')

def imprime_vertices_adjacentes(vertices):
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
  if opcao == 1:
    nome_grafo = input('Digite nome do grafo: ')
    direcionado = input('É direcionado?(s ou n) ')
    while direcionado != 's' and direcionado != 'n':
      direcionado = input('Digite \'s\' ou \'n\': ')
    if direcionado == 's':
      ehDirecionado = True
    else:
      ehDirecionado = False
    global grafo
    grafo = Grafo(nome_grafo, ehDirecionado)
  elif opcao == 2:
    vertices = input('Digite os vértices: ')
    grafo.criar_vertices(vertices)
  elif opcao == 3:
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
  elif opcao == 4:
    imprime_arestas('Arestas existentes: ', grafo.arestas)
    id_aresta = input('Digite o id da aresta: ').upper()
    aresta_deletada = grafo.deleta_aresta(id_aresta)
    if not(aresta_deletada):
      print('A aresta deve ter sido criada para realizar essa ação')
  elif opcao == 5:
    imprime_vertices('Vértices criados: ', grafo.vertices)
    id_vertice = input('Digite o id do vértice: ')
    grafo.deleta_vertice(id_vertice)
  elif opcao == 7:
    id_vertice = input('Digite o id do vértice: ').upper()
    vertices_adjacentes = grafo.get_vertices_adjacentes(id_vertice)
    imprime_vertices('Vértices adjacentes ao vértice {}:'.format(id_vertice), vertices_adjacentes)
  elif opcao == 14:
    print("Grafo: " + grafo.nome + "\n")
    imprime_vertices('Vértices existentes: ', grafo.vertices)
    imprime_arestas('Arestas existentes: ', grafo.arestas)
  else:
    print('Xau')

def display_menu():
  print('''
  1 - Criar grafo
  2 - Inserir vértices
  3 - Inserir aresta
  4 - Remover aresta
  5 - Remover vértices
  6 - Testar existência de aresta entre dois vértices
  7 - Obter os vértices adjacentes a um determinado vértice
  8 - Obter o grau de um determinado vértice
  9 - Obter o grau médio, o grau mínimo e o grau máximo
  10 - Identifique se o grafo é conexo
  11 - Exibir Matriz de Adjacências
  12 - Verificar existência de um caminho de Euler
  13 - Ler entrada a partir de arquivo
  14 - Visualizar vertices e arestas
  15 - Sair\n''')

while opcao != 15:
  display_menu()
  opcao = int(input('Selecione uma opção: '))
  print('----------------------- \n')
  seleciona_funcionalidade(opcao)

# SETUP DE TESTES
# grafo = Grafo('Grafo 1')
# vertices = input('Digite os vértices')
# lista_vertice = grafo.criar_vertice(vertices)

# g.criar_vertice("A")
# g.criar_vertice("B")
# g.criar_vertice("C")
# g.criar_vertice("D")
# g.criar_aresta(0,2,0)
# print(g.get_arestas())