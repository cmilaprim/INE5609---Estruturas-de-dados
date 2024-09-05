class Fila:
    def __init__(self, max):
        self.__max = max
        self.__dados = []
        self.__inico = 0
        self.__fim = -1
        self.__qntdd = 0
    
    def entrar(self, valor):
        if self.__qntdd < self.__max:
            self.__fim += 1
            if self.__fim == self.__max:
                self.__fim = 0
            self.__dados[self.__fim] = valor
            self.__qntdd += 1
        else:
            return "Fila cheia"
    
    def sair(self):
        if self.__qntdd > 0:
            self.__qntdd -= 1
            ret = self.__dados[self.__inicio]
            self.__inicio += 1
            if self.__inicio == self.__max:
                self.__inicio = 0
            return ret
        else:
            return "Fila vazia"        