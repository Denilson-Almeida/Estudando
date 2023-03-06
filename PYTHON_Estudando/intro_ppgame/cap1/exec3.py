# Strings / Slicing / Métodos

# Formas ideais de usar '' e ""

print('Como foi "lá"? ')

print('Tudo bem e aqui?')

print("Hm, 'normal' eu diria.")

print("Que bom \"né\" ?")

print("""Como assim. "O quê?" """)

print("Excuse " + "me?")

print("Vou converter cinco em string. Veja! " + str(5))

print("Ehh? " * 10)

print()


# Fatiamento (Slicing) 'Fazendo parse de strings'
"""
# Escrever exemplo aqui, depois de saber como explicar. <<<

Exemplo: 
[0] T , [1] u , [2] b , [3] a , [4] r , [5] ã , [6] o , [7]  (espaço que vêm no fim)

"""
minha_string = 'tubarão'
print(minha_string)
print(minha_string[0])
print(minha_string[0:4])
print(minha_string[4:7])
print(minha_string[-1])
print(minha_string[::-1])
print(minha_string[2::])
print('Quantidade de Letras na Váriavel:', len(minha_string))
print((minha_string[0::2])) # Pega tudo desde o começo pulando de 2 em 2

print()


# Métodos em string (EXISTEM MUITAS OUTRAS!)
print(minha_string.title()) # Converte todas as primeiras letras da string em maiúsculas
print(minha_string.capitalize()) # Converte a primeira letra da string em maiúsculo
print(minha_string.upper()) # Converte a string em maiúsculo
print(minha_string.lower()) # Converte a string para minúsculo
