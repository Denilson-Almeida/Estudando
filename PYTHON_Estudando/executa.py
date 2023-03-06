
print((5 + 5) * 2 + (5 - 2) // 2)

print(3 // 2)

preco = 75
pratos = 2
gorjeta = 5

total = (preco * pratos) * (gorjeta / 100)
print(f"{total:.2f}, 'result'")

print(' "Hello", cara! ')
print(" \"Precisa da barra invertida\" ")

album = ['cd', 'asda', 'ddd']
album.append('Bla bla')

print(album)
del album[1]
print(len(album))
album.sort()
print(album.index('ddd'))

telefone = (11, int('923123213'))
ddd, numero = telefone

print(numero, ddd)
print(telefone)

filmes = {'Esquadrão Suicida': 9.99, 'Eu sou a Lenda': 1}
filmes['a'] = 2

print(filmes.items())
print(filmes)


outras_cores = {'preto': 444, 'branco': 555}

cores = {'red': 111, 'blue': 222, 'yellow': 333}

cores.update(outras_cores)
print(cores, '\n')

cont = 0
while cont <= 3:
    print(cont)
    cont += 1

for x in range(4, 8):
    print(x)

print(1 >= 2)

print(1 != 1)

print(1 == 2)

print(2 < 1)



    
