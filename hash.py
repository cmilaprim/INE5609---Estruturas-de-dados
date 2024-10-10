from lista import Lista
class Hash:
    def __init__(self, tamanho_da_tabela):
        self.tamanho_da_tabela = tamanho_da_tabela
        self.tabela = [None] * tamanho_da_tabela
    
    def get_hash(self, chave):
        valor = 0
        for numero in chave:
            valor += int(numero)
        return valor % self.tamanho_da_tabela

    def inserir(self, chave, valor):
        posicao = self.get_hash(chave)
        if self.tabela[posicao] == None:
            self.tabela[posicao] = Lista()
        self.tabela[posicao].inserirComoUltimo(valor)
    
    def remover(self, chave, valor):
        posicao = self.get_hash(chave)
        if self.tabela[posicao] != None:
            self.tabela[posicao].remover(valor)


hash_table = Hash(10)
print(hash_table.inserir([1,2,3], 10))
