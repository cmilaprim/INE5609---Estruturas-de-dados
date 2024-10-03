class Elemento:
    def __init(self, v):
        self.__valor = v
        self.__anterior = None
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def anterior(self):
        return self.__anterior
    
    @valor.setter
    def valor(self, v):
        self.__valor = v
    
    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior
    
class Pilha:
    def __init__(self):
        self.__topo = None
    
    def push(self, valor):
        novoElemento = Elemento(valor)
        novoElemento.anterior = self.__topo
        self.__topo = novoElemento
    
    def pop(self):
        if self.__topo != None:
            salva = self.__topo.valor
            self.__topo = self.__topo.anterior
            return salva
        else:
            return "Pilha vazia"

class Fila:
    
    def __init__(self):
        self.__inicio = None
        self.__fim = None
    
    def entra(self, valor):
        novoElemento = Elemento(valor)
        if self.__fim == None:
            self.__inicio = novoElemento
            self.__fim = novoElemento
        else:
            self.__fim.anterior = novoElemento
            self.__fim = novoElemento
    
    def sair(self):
        if self.__inicio != None:
            salva = self.__inicio.valor
            self.__inicio = self.__inicio.anterior
            return salva
        else:
            return "Fila vazia"