class Elemento:
    def __init__(self,data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
    
    def get_data(self):
        return self.data
    
    def setter_data(self, new_data):
        self.data = new_data

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = Elemento(None, None, None)
        self.fim = Elemento(None, None, None)
        self.inicio.next = self.fim
        self.fim.prev = self.inicio
        self.tamanho = 0
    
    def is_empty(self):
        return self.tamanho == 0

    def ___len__(self):
        return self.tamanho
    
    def inserirNoMeio(self, item, antecessor, sucessor):
        novo_elemento = Elemento(item, antecessor, sucessor)
        antecessor.next = novo_elemento
        sucessor.prev = novo_elemento
        self.tamanho += 1
        return novo_elemento
    
    def delete_elemento(self, elem):
        antecessor = elem.prev
        sucessor = elem.next
        antecessor.next = sucessor
        sucessor.prev = antecessor
        self.tamanho -= 1
        #isolar o elemento
        elemento = elem.data
        elem.prev = elem.next = None
        return elemento
    
    def inserirPrimeiro(self, data):
        self.inserirNoMeio(data, self.inicio, self.inicio.next)
    
    def inserirUltimo(self, data):
        self.inserirNoMeio(data, self.fim.prev, self.fim)
    
    def deleta_primeiro(self):
        if self.is_empty():
            return None
        return self.delete_elemento(self.inicio.next)
    
    def deleta_ultimo(self):
        if self.is_empty():
            return None
        return self.delete_elemento(self.fim.prev)
    
    def print_list(self):
        temp = self.inicio.next
        x = []
        while temp.next != None:
            x.append(temp.data)
            temp = temp.next
        return x