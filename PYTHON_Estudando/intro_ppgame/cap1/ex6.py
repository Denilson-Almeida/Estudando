# Dicionários

cores = {'red': 111, 'blue': 222, 'yellow': 333}

print(cores['yellow'])

print(cores.keys())

print(cores.values())

cores['verde'] = 444

print(cores)

outras_cores = {'preto': 444, 'branco': 555}

# Copiando a chave/valor de uma lista para outra (de outras_cores para cores)
cores.update(outras_cores)
print(cores)