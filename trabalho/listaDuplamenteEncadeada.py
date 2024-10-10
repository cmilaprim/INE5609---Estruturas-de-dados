from elemento import Elemento

class ListaDuplamenteEncadeada:
    def __init__(self, tamanho_lista):
        self.__comeco = None
        self.__final = None
        self.__cursor = None
        self.__numero_elementos = 0
        self.__tamanho_lista = tamanho_lista
    
    @property
    def tamanho_lista(self):
        return self.__tamanho_lista
    
    @property
    def comeco(self):
        return self.__comeco
    
    @property
    def final(self):
        return self.__final
    
    @property
    def numero_elementos(self):
        return self.__numero_elementos
    
    @property
    def cursor(self):
        return self.__cursor
    
    def lista_cheia(self):
        return self.__numero_elementos == self.__tamanho_lista
    
    def lista_vazia(self):
        return self.__numero_elementos == 0
    
    def acessar_atual(self):
        return self.__cursor.dado

    def __ir_para_primeiro(self):
        self.__cursor = self.__comeco
    
    def __ir_para_ultimo(self):
        self.__cursor = self.__final
    
    def __apenas_um_elemento(self):
        self.__comeco = self.__final = self.__cursor = None
    
    def __primeiro_elemento_inserido(self, dado):
        self.__comeco = self.__final = self.__cursor = dado
    
    def __avancar_p_posicoes(self, p):
        if p < 0 or p >= self.__numero_elementos:
            return 'Erro de posição'
        else:
            for _ in range(p):
                self.__cursor = self.__cursor.__sucessor   
    
    def __retroceder_p_posicoes(self, p):
        if p < 0 or p >= self.__numero_elementos:
            return 'Erro de posição'
        else:
            for _ in range(p):
                self.__cursor = self.__cursor.__antecessor
    
    def __buscar_pela_posicao(self, chave):
        contador_posicao = 0
        self.__ir_para_primeiro()
        while self.__cursor is not None:
            if self.__cursor.dado == chave:
                return contador_posicao
            elif self.__cursor == self.__final:
                break
            self.__cursor = self.__cursor.__sucessor
            contador_posicao += 1
        return None
    
    def inserir_como_primeiro(self, dado):
        if self.lista_cheia():
            return 'Lista Cheia'
        novo = Elemento(dado)
        if self.lista_vazia():
            self.__primeiro_elemento_inserido(novo)
        else:
            novo.__sucessor = self.__comeco
            self.__comeco.__antecessor = novo
            self.__comeco = novo
        self.__cursor = novo
        self.__numero_elementos += 1
    
    def inserir_como_ultimo(self, dado):
        if self.lista_cheia():
            return 'Lista Cheia'
        novo = Elemento(dado)
        self.__ir_para_ultimo()
        if self.lista_vazia():
            self.__primeiro_elemento_inserido(novo)
        else:
            novo.__antecessor = self.__final
            self.__final.__sucessor = novo
            self.__final = novo
        self.__cursor = novo
        self.__numero_elementos += 1
    
    def inserir_antes_do_atual(self, dado):
        if self.lista_cheia():
            return 'Lista Cheia'
        novo = Elemento(dado)
        if self.lista_vazia():
            self.__primeiro_elemento_inserido(novo)
        else:
            if self.__cursor == self.__comeco:
                novo.__sucessor = self.__cursor
                self.__cursor.__antecessor = novo
                self.__comeco = novo
            else:
                novo.__sucessor = self.__cursor
                novo.__antecessor = self.__cursor.__antecessor
                self.__cursor.__antecessor.__sucessor = novo
                self.__cursor.__antecessor = novo
        self.__cursor = novo
        self.__numero_elementos += 1
    
    def inserir_depois_do_atual(self, dado):
        if self.lista_cheia():
            return 'Lista Cheia'
        novo = Elemento(dado)
        if self.lista_vazia():
            self.__primeiro_elemento_inserido(novo)
        else:
            if self.__cursor == self.__final:
                novo.__antecessor = self.__cursor
                self.__cursor.__sucessor = novo
                self.__final = novo
            else:
                novo.__antecessor = self.__cursor
                novo.__sucessor = self.__cursor.__sucessor
                self.__cursor.__sucessor.__antecessor = novo
                self.__cursor.__sucessor = novo
        self.__cursor = novo
        self.__numero_elementos += 1
    
    def inserir_na_posicao(self, dado, p):
        if self.lista_cheia():
            return 'Lista Cheia'
        novo = Elemento(dado)
        if p == 0:
            self.inserir_como_primeiro(novo)
        elif p == self.__numero_elementos:
            self.inserir_como_ultimo(novo)
        else:
            self.__ir_para_primeiro()
            self.__avancar_p_posicoes(p)
            novo.__sucessor = self.__cursor
            novo.__antecessor = self.__cursor.__antecessor
            self.__cursor.__antecessor.__sucessor = novo
            self.__cursor.__antecessor = novo
            self.__cursor = novo
            self.__numero_elementos += 1
    
    def remover_primeiro(self):
        if self.lista_vazia():
            return 'Lista Vazia'
        if self.__numero_elementos == 1:
            self.__apenas_um_elemento()
        else:
            self.__comeco = self.__comeco.__sucessor
            self.__comeco.__antecessor = None
            self.__cursor = self.__comeco
        self.__numero_elementos -= 1
    
    def remover_ultimo(self):
        if self.lista_vazia():
            return 'Lista Vazia'
        if self.__numero_elementos == 1:
            self.__apenas_um_elemento()
        else:
            self.__final = self.__final.__antecessor
            self.__final.__sucessor = None
            self.__cursor = self.__final
        self.__numero_elementos -= 1
    
    def remover_atual(self):
        if self.lista_vazia():
            return 'Lista Vazia'
        if self.__numero_elementos == 1:
            self.__apenas_um_elemento()
        else:
            if self.__cursor == self.__comeco:
                self.remover_primeiro()
            elif self.__cursor == self.__final:
                self.remover_ultimo()
            else:
                self.__cursor.__antecessor.__sucessor = self.__cursor.__sucessor
                self.__cursor.__sucessor.__antecessor = self.__cursor.__antecessor
                self.__cursor = self.__cursor.__sucessor
        self.__numero_elementos -= 1
    
    def remover_da_posicao(self, p):
        if self.lista_vazia():
            return 'Lista Vazia'
        if self.__numero_elementos == 1:
            self.__apenas_um_elemento()
        elif p == 0:
            self.remover_primeiro()
        elif p == self.__numero_elementos - 1:
            self.remover_ultimo()
        else:
            self.__ir_para_primeiro()
            self.__avancar_p_posicoes(p)
            self.__cursor.__antecessor.__sucessor = self.__cursor.__sucessor
            self.__cursor.__sucessor.__antecessor = self.__cursor.__antecessor
            self.__cursor = self.__cursor.__sucessor
        self.__numero_elementos -= 1
    
    def remover_elemento(self, chave):
        p = self.__buscar_pela_posicao(chave)
        self.remover_da_posicao(p)
    
    def buscar_elemento(self, chave):
        p = self.__buscar_pela_posicao(chave)
        if p is not None:
            return f'Elemento encontrado!!! Está na posição {p}'
        else:
            return f'Elemento não encontrado!!!'

    def listar_elementos(self):
        if self.lista_vazia():
            return 'Lista Vazia'
        c = self.__comeco
        for _ in range(self.__numero_elementos - 1):
            print(c.dado, end=' ')
            c = c.__sucessor
        print(c.dado)
