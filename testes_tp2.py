from TP2 import *

with open('grafo_W_4.txt', 'r') as arquivo:  #mudar o número do grafo de acordo com o teste 
        texto = [vertice for vertice in arquivo.read().split()  ] #Cria uma lista com o conteúdo presente no arquivo de teste
        vertices = int(texto[0]) #Pega o primeiro elemento da lista acima, que correnspode ao número de vértices do grafo
        arestas = [] #Lista vazia que vai conter todos os pares de arestas do grafo
        for i in range(len(texto[1:])//3):
            arestas += [[int(texto[3*i+1])]+[int(texto[3*i+2])]+ [float(texto[3*i+3])]] 


grafo = Graph_l(vertices, arestas)

#Questão 1: (ir mudando v2 entre 20, 30, 40, 50 e 60)
v_teste = [20,30,40,50,60]
for vf in v_teste: 
    grafo.distancia(10,vf,1)  
    grafo.caminho(10,vf,1)       

#Questão 2: 

import time
import random

tempo_djk = 0
tempo_heap = 0 

for i in range(20):
    vertice = random.randint(1,grafo.v)
    
    inicio_djk = time.time()
    grafo.DijkstraHeap(vertice,0)
    fim_djk = time.time()

    inicio_heap = time.time()
    grafo.Dijkstra(vertice,0)
    fim_heap = time.time()
    
    tempo_djk += fim_djk - inicio_djk
    tempo_heap += fim_heap - inicio_heap

print ('Tempo sem heap:', tempo_djk/20, 'Tempo com heap:', tempo_heap/20)

#Questão 3 (Rede de colaboração):

with open('rede_colaboracao_vertices.txt', 'r', encoding='utf-8') as arquivo:
    colaboradores = [x.rstrip('\n').split(',') for x in arquivo.readlines()]
    dic = {}
    for i in range(len(colaboradores)):
        dic[colaboradores[i][1]] = int(i+1)
            
with open('rede_colaboracao.txt', 'r', encoding='utf-8') as arquivo:
        texto = [vertice for vertice in arquivo.read().split()  ] #Cria uma lista com o conteúdo presente no arquivo de teste
        vertices = int(texto[0]) #Pega o primeiro elemento da lista acima, que correnspode ao número de vértices do grafo
        arestas = [] #Lista vazia que vai conter todos os pares de arestas do grafo
        for i in range(len(texto[1:])//3):
            arestas += [[int(texto[3*i+1])]+[int(texto[3*i+2])]+ [float(texto[3*i+3])]] #Atualiza a lista de arestas, criando sublistas com os pares de arestas


G = Graph_l(vertices, arestas)
origem = 'Edsger W. Dijkstra'
pesquisadores = ['Alan M. Turing', 'J. B. Kruskal', 'Jon M. Kleinberg', 'Daniel R. Figueiredo', 'Éva Tardos']


for i in range(len(pesquisadores)):
    d = G.distancia(dic[origem], dic[pesquisadores[i]], 0)
    caminho_min = G.caminho(dic[origem], dic[pesquisadores[i]], 0)
    print(f'Distância entre {origem} e {pesquisadores[i]}: {d}')
    print(f'Caminho minimo entre {origem} e {pesquisadores[i]}: {caminho_min}')
