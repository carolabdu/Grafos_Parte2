from TP2 import *

def infos_grafo(arq, representacao, bfs=False, dfs=False, dist=False, diameter=False, cc=False):   #Função para obter as informações do grafo escolhido
    with open(f'{arq}.txt', 'r') as arquivo:
        texto = [int(vertice) for vertice in arquivo.read().split() if vertice.isdigit()] #Cria uma lista com o conteúdo presente no arquivo de teste
        vertices = texto[0] #Pega o primeiro elemento da lista acima, que correnspode ao número de vértices do grafo
        arestas = [] #Lista vazia que vai conter todos os pares de arestas do grafo
        for i in range(1,len(texto[1:]), 3):
           arestas += [[int(texto[3*i+1])]+[int(texto[3*i+2])]+ [float(texto[3*i+3])]] #Atualiza a lista de arestas, criando sublistas com os pares de arestas

    
    if representacao=='L':
        resultado = open(f'Resultado_{arq}.txt', 'a', encoding='UTF-8')
        resultado.write(f'\nArquivo de grafo analisado:{arq}\nRepresentação por lista\n')
        grafo_lista = Graph_l(vertices, arestas)
        grafo_lista.arestas(1)
        grafo_lista.vertices(1)
        grafo_lista.graumin(1)
        grafo_lista.graumax(1)
        grafo_lista.graumed(1)
        grafo_lista.mediano(1)
        if bfs != False:
            grafo_lista.BFS(bfs, 1)
        if dfs != False:
            grafo_lista.DFS(dfs, 1)
        if dist != False:
            grafo_lista.distancia(dist[0], dist[1], 1)
        if diameter != False:
            grafo_lista.diameter(1)
        if cc != False:
            grafo_lista.cc(1)
        resultado.writelines(grafo_lista.arquivo_saida)
        resultado.close()
        
        
    elif representacao=='M':
        resultado = open(f'Resultado_{arq}.txt', 'a', encoding='UTF-8')
        resultado.write(f'\nArquivo de grafo analisado:{arq}\nRepresentação por matriz\n')
        grafo_matriz = Graph_m(vertices, arestas)
        grafo_matriz.arestas(1)
        grafo_matriz.vertices(1)
        grafo_matriz.graumin(1)
        grafo_matriz.graumax(1)
        grafo_matriz.graumed(1)
        grafo_matriz.mediano(1)
        if bfs != False:
            grafo_matriz.BFS(bfs, 1)
        if dfs != False:
            grafo_matriz.DFS(dfs, 1)
        if dist != False:
            grafo_matriz.distancia(dist[0], dist[1], 1)
        if diameter != False:
            grafo_matriz.diameter(1)
        if cc != False:
            grafo_matriz.cc(1)
        resultado.writelines(grafo_matriz.arquivo_saida)
        resultado.close()


