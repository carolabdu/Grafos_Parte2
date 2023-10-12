class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):   #adiciona vértice
         self.items.append(item)

     def pop(self):  #retira vértice
         return self.items.pop()

     def peek(self):   #retorna o topo da pilha
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
