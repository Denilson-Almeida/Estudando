# Alguns módulos: sin, cos, tan, ceil, fabs, floor, pi, datime

from datetime import datetime
import random

hora = datetime.now()
hora.ctime() # ctime() mostra de forma mais legível a hora na forma de string


for _ in range(5):  # Aqui é possível usar _ assim perde menos tempo pensando em um nome (Nem sabia)
    print(random.randint(1, 10))

print()

random.seed(100)

for roll in range(10):
    print(random.randint(1, 6))

print("Re-seeded")
random.seed(100)

for roll in range(10):
    print(random.randint(1, 6))

# Módulo Random, muito útil! 
# seed: Fornece uma semente ao gerador de números aleatórios,
# randint: Retorna um inteiro aleatório entre dois valores,
# choice: Seleciona um elemento aleatório em uma coleção, 
# random: Retorna um número de ponto flutuante entre 0 e 1