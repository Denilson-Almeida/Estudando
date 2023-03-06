# Loops
"""

"""

# Loop While
count = 1
while count <= 5:
    print(count)
    count += 1


# Loop For
for x in range(1, 11):
    print(x)

for y in range(3):
    print(y)


# Exemplo
feira = ['pastel', 'cana']
preco = {'pastel': 7.00, 'cana': 5.00}
total = 0

for item in feira:          # Pra cada item na lista
    total += preco[item]    # Total(0) += pra cada value de preco no dicionario soma ao 'total
print('Total:', total)