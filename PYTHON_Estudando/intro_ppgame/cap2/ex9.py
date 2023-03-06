# Estrutura de Condição (if, elif, else) e Operadores Lógicos (AND, OR, NOT)

print('\nEstrutura de Condição\n')

a = int(input('Digita um valor: '))
if a > 5:
    print('O valor é maior que 5')

elif a == 5:
    print('O valor é IGUAL a 5')

else:
    print('O valor é menor que 5')


print('\nOperadores Relacionais\n')

num = int(input('Digite um valor: '))
if num <= 5 or num == 25:
    print('OR')

if num > 35 and num < 41:
    print('(AND)')

if not 100 != num:
    print('NOT')

else:
    print('Não foi tratado.')


# Exemplificado
if 1 < 2 and 2 != 3:
    print('tudo certo')

if not 2 > 3 or 6 != 6:
    print('not e or?')