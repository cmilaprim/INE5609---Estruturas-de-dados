from listaDuplamenteEncadeada import ListaDuplamenteEncadeada

# Criando a lista
l = ListaDuplamenteEncadeada(9)


print("----- INSERINDO ELEMENTOS -----")
l.inserir_antes_do_atual(89)
l.inserir_antes_do_atual(78)
l.inserir_antes_do_atual(3)
print(f'Acessando o atual: {l.acessar_atual()}') 
l.inserir_antes_do_atual(12)
l.inserir_depois_do_atual(100)
l.inserir_como_primeiro(99)
l.inserir_como_ultimo(6)
l.listar_elementos()
l.inserir_na_posicao(8, 2)
l.listar_elementos()

print("----- REMOVENDO ELEMENTOS -----")
print(f'Acessando o atual: {l.acessar_atual()}') 
l.listar_elementos()
l.remover_atual()
l.listar_elementos()
l.remover_primeiro()
l.listar_elementos()
l.remover_elemento(100)
l.listar_elementos()
l.remover_ultimo()
l.listar_elementos()
l.remover_da_posicao(2)
print(l.acessar_atual())
l.listar_elementos()

print("----- BUSCANDO ELEMENTOS -----")
print(l.buscar_elemento(12))
print(l.buscar_elemento(1000000))
