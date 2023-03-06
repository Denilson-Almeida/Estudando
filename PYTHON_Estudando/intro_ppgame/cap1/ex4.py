# Listas

filmes = ['Eu sou a Lenda', 'Eu sou a Lenda 2']

series = ['TWD', 'Noite de Crime']

filmes.append('Toy Story')

print(filmes)

print(filmes[0])
print(filmes[0:2])
del filmes[1]
print(filmes)
print('Qnt.Filmes:',len(filmes))

print(series)
filmes += series # Adiciona os itens da lista 'series' em 'filmes'
print(filmes)
filmes.sort()
print(filmes)
filmes.pop(0)
print(filmes)

# Métodos de lista: append, count, extend, index, insert, pop, remove, reverse, sort