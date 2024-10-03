class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def proximo(self):
        return self.__proximo
    
    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserirComoPrimeiro(self, valor):
        novoElemento = Elemento(valor)
        if self.inicio == None:
            self.inicio = novoElemento
            self.fim = novoElemento
        else:
            novoElemento.proximo = self.inicio
            self.inicio = novoElemento
    
    def inserirComoUltimo(self,valor):
        novoElemento = Elemento(valor)
        if self.inicio == None:
            self.inicio = novoElemento
            self.fim = novoElemento
        else:
            self.fim.proximo = novoElemento
            self.fim = novoElemento

    def inserirNaPosicao(self, valor, posicao):
        if posicao == 0:
            self.inserirComoPrimeiro(valor)
        elif posicao == self.tamanho:
            self.inserirComoUltimo(valor)
        else:
            novoElemento = Elemento(valor)
            anterior = self.inicio
            for i in range(1, posicao):
                anterior = anterior.proximo
            novoElemento.proximo = anterior.proximo
            anterior.proximo = novoElemento
        self.tamanho += 1
    
    def inserirAntesDe(self, valor, referencia):
        if referencia == self.inicio:
            self.inserirComoPrimeiro(valor)
        else:
            novoElemento = Elemento(valor)
            anterior = self.inicio
            while anterior.proximo != referencia:
                anterior = anterior.proximo
            novoElemento.proximo = anterior.proximo
            anterior.proximo = novoElemento
        self.tamanho += 1
    
    def inserirDepoisDe(self, valor, referencia):
        novoElemento = Elemento(valor)
        novoElemento.proximo = referencia.proximo
        referencia.proximo = novoElemento
        if referencia == self.fim:
            self.fim = novoElemento
        self.tamanho += 1
    
    def removerPrimeiro(self):
        if self.inicio != None:
            salva = self.inicio.valor
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return salva
        else:
            return "Lista vazia"
    
    def removerUltimo(self):
        if self.fim != None:
            salva = self.fim.valor
            self.fim = self.fim.proximo
            self.tamanho -= 1
            return salva
        else:
            return "Lista vazia"
    
    def removerNaPosicao(self, posicao):
        if posicao == 0:
            return self.removerPrimeiro()
        elif posicao == self.tamanho - 1:
            return self.removerUltimo()
        else:
            anterior = self.incio
            for i in range(1, posicao):
                anterior = anterior.proximo
            salva = anterior.proximo.valor
            anterior.proximo = anterior.proximo.proximo
            self.tamanho -= 1
            return salva
    
    def remover(self, referencia):
        if referencia == self.inicio:
            return self.removerPrimeiro()
        elif referencia == self.fim:
            return self.removerUltimo()
        else:
            anterior = self.inicio
            while anterior.proximo != referencia:
                anterior = anterior.proximo
            salva = anterior.proximo.valor
            anterior.proximo = anterior.proximo.proximo
            self.tamanho -= 1
            return salva
    
    def acessaPrimeiro(self):
        if self.inicio != None:
            return self.inicio.valor
        else:
            return "Lista vazia"
    
    def acessaUltimo(self):
        if self.fim != None:
            return self.fim.valor
        else:
            return "Lista vazia"
    
    def acessarDaPosicao(self, posicao):
        if posicao == 0:
            return self.acessaPrimeiro()
        elif posicao == self.tamanho - 1:
            return self.acessaUltimo()
        else:
            elemento = self.inicio
            for i in range(posicao):
                elemento = elemento.proximo
            return elemento.valor
        
    
    def exibirLista(self):
        elementos = []
        atual = self.inicio
        while atual != None:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos
        

lista = Lista()
lista.inserirComoPrimeiro(10)
lista.inserirComoUltimo(20)
lista.inserirComoUltimo(30)
lista.inserirNaPosicao(15, 1)
lista.inserirNaPosicao(25, 3)
lista.inserirNaPosicao(35, 5)
lista.inserirAntesDe(5, lista.inicio)
lista.removerNaPosicao(0)
print(lista.acessarDaPosicao(5))
print(lista.exibirLista()) 