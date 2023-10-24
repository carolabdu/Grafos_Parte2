# Trabalho_Grafos
Essa biblioteca pode fornecer as seguintes informações:

1. Informações básica como:
     - Número de arestas do grafo
     - Número de vértices do grafo
2. Tipo de reprensentação (Lista de Adjacência)
3. Resultados do algoritmo de Dijkstra (distâncias a um vértice inicial, e árvore geradora)
4. Menor caminho possível entre dois vértices
Obs: As informações 3 e 4 só são geradas quando não há pesos negativos, caso contrário é informado ao usuário que não é possível gerar os resultados. 

## Uso da biblioteca:

Para acessar as informações detalhadas acima, criamos um código para transforma o arquivo de texto em 'vertices' e 'arestas' (no arquivo testes_tp2.py) que funcionam como parâmetros para a classe Graph_l. 

Depois, basta criar o grafo desejado e usar normalmete a classe. 
Por exemplo: 
grafo = Graph_l(vertices, arestas)
Para ver a distância entre v1 e v1: grafo.distancia(v1,v2,p) 




