# Funções

# Defini o default dos parâmetros. Pq? Pq sim! "Default" é o valor pré-definido na função.
def calcula_gorjeta(preco=100, pratos=2, gorjeta=15): # 'gorjeta' representa uma porcentagem do valor da comida
    total = (preco * pratos) * (gorjeta / 100)
    print(total)

calcula_gorjeta()

""" 
Normalmente um objeto têm "parâmetros", "propriedades" e "métodos".

Parâmetros: são valores que devemos passar (ou não) para determinado objeto

Propriedades: são o que descrevem/definem o objeto inicial (o "esqueleto" que todos os objetos adjacentes terão)

Métodos: são as funções (basicamente as "ações" que o objeto pode fazer)
"""