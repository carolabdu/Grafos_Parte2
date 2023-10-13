import numpy as np
import random
from stack import *
from queue import *


class Graph_l:
    def __init__(self, v, a): #(número de vértices, arestas)
        self.aqruivo_saida = [] #Lista que vai receber os resultados desejados
        self.v = v
        self.a = a
        self.num_arestas = len(self.a) 
        self.neg = False
        self.lista = [[] for i in range(self.v)] #Não sabemos quantos elementos tem em cada linha (quantos vizinhos cada vértice tem)
        self.pesos = [[] for i in range(self.v)]  #lista que contém apenas os pesos 
        g = np.zeros(self.v,dtype=int) #Vetor de zeros, onde vamos guardar o grau de cada vértice
        for i in range(self.num_arestas):
            u=self.a[i][0] #Pega o primeiro vértice do par de arestas
            v= self.a[i][1] #Pega o segundo vértice do par de arestas
            p= self.a[i][2] #Pega o peso da aresta
            if p < 0: self.neg = True
            self.lista[u-1]+= [(v,p)] #Adiciona o vértice v na linha u (o índice é u-1, pois i se inicia no 0)
            self.lista[v-1]+= [(u, p)] #Adiciona o vértice u na linha v
            self.pesos[u-1]+= [p]
            self.pesos[v-1] += [p]
            g [u-1] += 1  #Atualiza os graus 
            g [v-1] += 1
        self.graus = g

    #Algumas funções possuem o padrão "p", que define se o resultado dele ser escrito no arquivo de saída ou não
    def vertices(self,p): #Retorna o número de vértices do grafo 
        if p ==1:
            self.arquivo_saida.append(f'\nNúmero de vértices: {self.v}')
        return self.v 
    
    def arestas(self,p): #Retorna o número de arestas do grafo
        a = int(np.sum(self.graus))/2 #Usamos a relação: Grau = 2*#Arestas
        if p==1:
            self.arquivo_saida.append(f'\nNúmero de arestas: {int(a)}')
        return a

    def mostra_lista(self): #Retorna a lista de adjacência
        return self.lista 
    
    def mostra_grau(self): #Retorna a lista de graus
        return self.graus

    def graumin(self,p): #Retorna o grau mínimo
        grau_min = np.min(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau mínimo: {grau_min}')
        return grau_min

    def graumax(self,p): #Retorna o grau máximo
        grau_max = np.max(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau máximo: {grau_max}')
        return grau_max
        
    def graumed(self,p): #Retorna a média dos graus
        grau_med = np.mean(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau médio: {grau_med}')
        return grau_med

    def mediano(self,p):
        mediano = np.median(self.graus)
        if p==1: 
            self.arquivo_saida.append(f'\nMediana dos graus: {mediano}')
        return int(mediano)

    def distancia(self, v1, v2, p): #Retorna a distâncoa entre dois vértices
        D= self.Dijkstra(v1, 0)[0][v2-1]
        if p==1:
            self.arquivo_saida.append(f'\nDistância entre {v1} e {v2}: {D}')
        return D


    def Dijkstra(self,vi, p):
        if self.neg == True:
            print('not possble') 
            d = 'Não é possível'
        else:  
            pai = np.array([-1] * self.v, dtype = int) #inicia vetor com os pais
            nivel = np.array([-1] * self.v, dtype = int) #inicia vetor dos níveis
            S = np.zeros(self.v) #Definir S como vazio
            len_S = 0 #variável auxiliar para não ter que verificar a cada iteração a lista S
            dist = np.full(self.v, np.inf) #distâncias começam infinitas
            dist_aux = np.full(self.v, np.inf)
            dist_aux[vi-1]=0 
            pai [vi-1] = 0
            nivel [vi-1] = 0 
            while len_S != self.v : #Enquanto S != V
                p_u = np.min(dist_aux) #Selecione u em V-S, tal que dist[u] é mínima
                u = np.argmin(dist_aux) #u que tem a distância mínima
                if p_u == np.inf :   #grafo não é conexo
                    break
                S[u]= 1 #Adicione u em S
                len_S += 1 
                dist[u]=dist_aux[u]
                dist_aux[u]= np.inf  #usado para que não alteremos mais a distância de quem já foi adicionado a S
                for viz in range(len(self.lista[u])): #Para cada vizinho de u faça
                    v = self.lista[u][viz][0]
                    if S[v-1] ==0: 
                        if dist_aux[v-1] > dist[u] + self.lista[u][viz][1] :  #Se dist[v] > dist[u] + w(u,v) então
                            dist_aux[v-1] = dist[u] + self.lista[u][viz][1] #dist[v] = dist[u] + w(u,v)
                            pai[v-1] = u+1
                            nivel[v-1] = nivel[u] + 1
            d = [dist, pai, nivel] 
            if p ==1: 
                self.arquivo_saida.append(f'\nDijkstra a partir de {v1} : {d[0]}, árvore (pais): {d[1]}, árvore(níveis): {d[2]} ')
        return d    

    def caminho(self,v1,v2,p): #v1 é o vértice de partida, v2 o de chegada e p é para imprimir 
        pais = self.Dijkstra(v2, 0)[1]  #fazemos a árvore a partir de v2, para ir encontrando os pais de v1 até chegar em v2
        caminho = [v1] #caminho começa já com o vétice de partida
        v= v1  #começamos em v1
        while v != v2: #enquanto vértice analisado não for vértice destino 
            v = pais [v-1]  #próximo vértice do caminho é o pai do que último adicionado 
            caminho.append(v)   #adicionamos esse pai ao caminho
        if p==1:
            self.arquivo_saida.append(f'\nCaminho entre  {v1} e {v2}: {caminho} ')
        return caminho 
    

class Graph_m: #grafo em matriz 
    def __init__(self, v, a):
        self.arquivo_saida = []
        self.v = v
        self.a = a   #mudar forma de como guardar uasando numpy
        self.matriz = np.zeros([self.v, self.v], dtype=int)
        for i in range(len(self.a)):
            v1= self.a[i][0]
            v2= self.a[i][1]
            self.matriz[v1-1][v2-1] = self.a[i][2] #se os vértices estão conecatados 
            self.matriz[v2-1][v1-1]= self.a[i][2] #grafo não é direcionado, 'espelhamos' o resultado

    def vertices(self,p):
        if p==1:
             self.arquivo_saida.append(f'\nNúmero de vértices: {self.v}')
        return self.v

    def arestas(self,p):
        if p==1:
            self.arquivo_saida.append(f'\nNúmero de arestas: {int(len(self.a))}')
        return len(self.a)
    
    def mostra_matriz(self):
        for i in range(self.v):
            print(self.matriz[i])    
    
    #def grau (self,p):
        #graus = np.sum(self.matriz, axis=0)
        #print(graus)

    def graumin(self,p):
        graus = np.sum(self.matriz, axis=0)
        grau_min = np.min(graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau mínimo: {grau_min}')
        return grau_min

    def graumax(self, p):
        graus = np.sum(self.matriz, axis=0)
        grau_max = np.max(graus)
        if p==1:
          self.arquivo_saida.append(f'\nGrau máximo: {grau_max}')
        return grau_max
        
    
    def graumed(self, p):
        graus = np.sum(self.matriz, axis=0)
        soma_graus = np.sum(np.sum(self.matriz, axis=0), axis=0)
        grau_med = (soma_graus/self.v)
        if p==1:
            self.arquivo_saida.append(f'\nGrau médio: {grau_med}')
        return grau_med

    def mediano(self,p):
        graus = np.sum(self.matriz, axis= 0)
        mediano = np.median(graus)
        if p==1:
            self.arquivo_saida.append(f'\nMediana dos graus: {mediano}')
        return int(mediano)


    def DFS(self,vi,p):
        self.marcados = np.zeros(self.v,dtype=int) #inicia vetor de marcação
        self.s = Stack() #cria pilha vazia
        self.s.push(vi)  #adiciona a raiz na pilha
        pai = np.array([-1] * self.v, dtype = int) #inicia vetor com os pais
        nivel = np.array([-1] * self.v, dtype = int) #inicia vetor dos níveis
        pai[vi-1] = 0 #indica que não tem pai pois é raiz
        nivel[vi -1]= 0 #nivel da raiz é zero 
        while self.s.isEmpty()==False : #enquanto pilha não estiver vazia 
            u = self.s.peek() #pega vértice no topo da lista
            self.s.pop() #remover u da pilha 
            if self.marcados[u-1]==0: # (implemetar para ver se tá na lista): 
                self.marcados[u-1]=1 #adicionar vétice aos marcados
                for k in range(self.v): #para cada vizinho de u 
                    vizinho = self.matriz[u-1][k] #verificar se elemento da matriz é 1
                    if vizinho ==1: #ou seja se é vizinho de fato
                        self.s.push(k+1)  #botar na fila 
                        if self.marcados[k]==0:  #se k ainda não foi marcado
                            pai[k] = u   #escrevre que u descobriu (vai mudando ao longo do algoritmo)
                            nivel[k] = nivel[u-1] + 1  #verifica o nível do pai de k e soma 1
        self.DFStree = [pai, nivel]
        if p==1: 
           self.arquivo_saida.append(f'\nBusca DFS:\nPais: {pai}\nNíveis: {nivel}')
        return (self.DFStree)

    def BFS(self,vi,p):
        self.marcados = np.zeros(self.v,dtype=int) #Lista com os vétices explorados
        self.Q = Queue() #Cria uma fila vazia
        pai = np.array([-1] *self.v, dtype = int) #Inicia vetor com os pais
        nivel = np.array([-1] * self.v, dtype = int) #Inicia vetor dos níveis
        pai[vi-1] = 0 #Indica que não tem pai pois é raiz
        nivel[vi-1] =0 
        self.marcados[vi-1]=1 #Marca o vértice inicial
        self.Q.add(vi) #Adiciona o primeiro vértice à primeira posição da fila
        pai[vi-1] = 0 #indica que é raiz 
        while self.Q.is_empty() == False: #A busca continua enquanto a fila não estiver vazia
            v = self.Q.pop() #Remove o último vértice
            for w in range(self.v): #para cada vizinho de v
                    vizinho = self.matriz[v-1][w] #verificar se elemento da matriz é 1
                    if vizinho ==1: 
                        if self.marcados[w]==0: 
                            pai[w]= v #Coloca v como pai de w, que o descobriu
                            nivel[w] = nivel[v-1]+1 #Muda o nível para o nível de w
                            self.marcados[w]=1 #Marca w
                            self.Q.add(w+1) #Adiciona w na primeira posição da fila
                            
        self.maxlevel = np.max(nivel) #Pega o maior nível
        self.BFStree = [pai, nivel,self.maxlevel]
        if p==1: 
            self.arquivo_saida.append(f'\nBusca BFS:\nPais: {pai}\nNíveis: {nivel}')
        return (self.BFStree)

    def distancia(self, v1, v2,p): #Retorna a distância entre dois vértices
        self.BFS(v1,0) #Roda a BFS para v1
        if self.BFStree[0][v2 -1] == -1: #Se o pai de v2 for -1, ele não está conectado com v1
            distancia = 'infinita' #ou seja vértices não estão conectadas
        else: 
            distancia = self.BFStree[1][v2-1] #O nível de v2 será a distância dele até v1
        if p==1:
            self.arquivo_saida.append(f'\nDistância entre {v1} e {v2}: {distancia}')
        return distancia  

    def diameter(self, p): #Retorna o diâmetro do grafo
        if self.v < 1000: 
            diameter = 0
            for i in range(1,self.v):
                self.BFS(i,0) #Roda a BFS para cada um dos vértices
                if self.maxlevel > diameter:
                    diameter = self.maxlevel #Assume como diâmetro o maior nível
        else: 
            for i in range(1000):
                vi = random.randint(1, self.v) #Faz o mesmo que acima, porém para 1000 vértices aleatórios
                diameter = 0
                self.BFS(vi,0)
                if self.maxlevel > diameter:
                    diameter = self.maxlevel
        if p==1:
            self.arquivo_saida.append(f'\nDiâmetro do grafo: {diameter}')
        return diameter

    def cc(self,p):  #Retorna a quantidade de componentes conexas, a quantidade de nós da maior delas e da menor
        cc = []
        vistos = np.zeros(self.v,dtype=int) #Vetor de zeros
        for vi in range(1,self.v +1):
            if vistos[vi-1] == 0: 
                marcados = [[],0]  #Retorna os marcados e o tamanho da cc
                pais_vi = self.BFS(vi,0)[0] 
                for k in range(self.v):
                    if pais_vi[k] != -1:
                        vistos[k] = 1
                        marcados[0].append(k+1) #índice é uma unidade menor que o vétice
                        marcados[1] += 1
                cc.append(marcados[1])
        fim = np.asarray(cc)
        if p==1: 
             self.arquivo_saida.append(f'\nNúmero de componentes conexas no grafo: {len(fim)}\nMaior componente conexa: {np.max(fim)}\nMenor componente conexa: {np.min(fim)}')
        return cc    

    
  

    

