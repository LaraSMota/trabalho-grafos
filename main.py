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
  #DELETAR ARESTA
  elif opcao == 4:
    imprime_arestas('Arestas existentes: ', grafo.arestas)
    id_aresta = input('Digite o id da aresta: ').upper()
    aresta_deletada = grafo.deleta_aresta(id_aresta)
    if not(aresta_deletada):
      print('A aresta deve ter sido criada para realizar essa ação')
  elif opcao == 5:
    v1 = input('Digite o id do primeiro vértice: ').upper()
    v2 = input('Digite o id do segundo vértice: ').upper()
    resposta = grafo.exite_aresta_entre_vertices(v1, v2)
    print('\n', resposta['msg'])
  elif opcao == 6:
    id_vertice = input('Digite o id do vértice: ').upper()
    vertices_adjacentes = grafo.get_vertices_adjacentes(id_vertice)
    imprime_vertices_adjacentes('Vértices adjacentes ao vértice {}:'.format(id_vertice), vertices_adjacentes)
  elif opcao == 13:  #IMPRIME VERTICES E ARESTAS
    print("Grafo: " + grafo.nome + "\n")
    imprime_vertices('Vértices existentes: ', grafo.vertices)
    imprime_arestas('Arestas existentes: ', grafo.arestas)
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
  14 - Sair\n''')

print("Seja bem vindo! \n")
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

while opcao != 14:
  display_menu()
  opcao = int(input('Selecione uma opção: '))
  print('----------------------- \n')
  seleciona_funcionalidade(opcao)

print("FIM DE EXECUÇÃO")
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