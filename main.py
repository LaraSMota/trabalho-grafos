from grafo import *

opcao = 0

def imprime_vertices(vertices):
  v_concatenado = ''
  for v in vertices:
    v_concatenado += (v.id + ' ')
  print('Vértices criados: ', v_concatenado, '\n')

def imprime_arestas(arestas):
  a_concatenado = ''
  for a in arestas:
    a_concatenado += (a.id + ' ')
  print('Arestas criadas: ', a_concatenado, '\n')

def seleciona_funcionalidade(opcao):
  if opcao == 1:
    nome_grafo = input('Digite nome do grafo: ')
    direcionado = input('É direcionado?(y ou n) ')
    while not(direcionado != 'y' or direcionado != 'n'):
      direcionado = input('Digite \'y\' ou \'n\' ')
    if direcionado == 'y':
      ehDirecionado = True
    else:
      ehDirecionado = False
    global grafo
    grafo = Grafo(nome_grafo, ehDirecionado)
  elif opcao == 2:
    vertices = input('Digite os vértices: ')
    grafo.criar_vertices(vertices)
  elif opcao == 3:
    imprime_vertices(grafo.get_vertices())
    aresta_criada = False
    while aresta_criada == False:
      print('OBS: Ambos os vértices devem existir')
      print('------------------------------------')
      id = input('Digite um identificador para a aresta: ')
      vertice_1 = input('Digite o vertice 1: ')
      vertice_2 = input('Digite o vertice 2: ')
      peso = int(input('Digite o peso: '))
      aresta_criada = grafo.criar_aresta(id, vertice_1, vertice_2, peso)
  elif opcao == 4:
    imprime_arestas(grafo.arestas)
    id_aresta = input('Digite o id da aresta: ')
    aresta_deletada = grafo.deleta_aresta(id_aresta)
    print(aresta_deletada)
    if not(aresta_deletada):
      print('A aresta deve ter sido criada para realizar essa ação')
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
  14 - Sair\n''')

while opcao != 14:
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