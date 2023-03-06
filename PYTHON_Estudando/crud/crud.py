compras = ['abra', 'bala', 'cakra']

def adiciona(palavra):
    compras.append(palavra)

def checar(palavra):
    for valor in compras:
        if valor == palavra:
            print('Achei a palavra: ', valor)

def ver_lista():
    print('Ver Lista: ', compras)
    
def excluir(palavra):
    if palavra in compras:
        compras.remove(palavra)
    print(f'\nLista atualizada: {compras}\nPalavra excluída: {palavra}\n')

ver_lista()
adiciona('kkk')
ver_lista()
checar('kkk')
ver_lista()
excluir('bala')