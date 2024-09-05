class Pilha:
    
    def __init__(self, tamanhoMax):
        self.__tamanhoMax = tamanhoMax
        self.__dados = []
        # self.__topo = 0
        
    # def push(self, valor):
    #     if self.__topo - self.__tamanhoMax != 0:
    #         self.__dados[self.__topo] = valor
    #         self.__topo += 1
    #     else:
    #         return "Pilha cheia"
    
    # def pop(self):
    #     if self.__topo > 0:
    #         self.__topo -= 1
    #         return self.__dados[self.__topo]
    #     else:
    #         return "Pilha vazia"
    def push(self, valor):
        if len(self.__dados) < self.__tamanhoMax:
            self.__dados.append(valor)
        else:
            return "Pilha cheia"    
    
    def pop(self):
        if len(self.__dados) > 0:
            return self.__dados.pop()
        else:
            return "Pilha vazia"