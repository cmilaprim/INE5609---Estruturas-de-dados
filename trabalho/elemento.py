class Elemento:
    def __init__(self, dado, antecessor=None, sucessor=None):
        self.__dado = dado
        self.__antecessor = antecessor
        self.__sucessor = sucessor
    
    @property
    def dado(self):
        return self.__dado
    
    @property 
    def antecessor(self):
        return self.__antecessor

    @property
    def sucessor(self):
        return self.__sucessor