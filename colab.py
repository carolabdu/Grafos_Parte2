from TP2 import *
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
     G.distancia(dic[origem], dic[pesquisadores[i]], 1)
    

'''



Calcule a distˆancia e o caminho m´ınimo entre Edsger W. Dijkstra (o pesquisador) e os
seguintes pesquisadores da rede de colabora¸c˜ao: Alan M. Turing, J. B. Kruskal, Jon M.
Kleinberg, Eva Tardos, Daniel R. Figueiredo. Utilize exatamente estes nomes (strings) ´
para identificar os ´ındices dos v´ertices no grafo.
'''
