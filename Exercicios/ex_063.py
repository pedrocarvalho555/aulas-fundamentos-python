from random import randint

numchaves = int(input('Digite quantas chaves quer: '))
temp = list()
temp_chaves = list()
numeroEuromillions = list()

for c in range (0, numchaves):
    i = 0
    while i != 5:
        intervalo = randint(1, 50)
        if temp.count(intervalo) == 0:
            temp.append(intervalo)
            i += 1

    i = 0

    while i != 2:
        chaves = randint(1, 12)
        if temp_chaves.count(chaves) == 0:
            temp_chaves.append(chaves)
            i += 1

    numeroEuromillions.append(temp[:])
    numeroEuromillions.append(temp_chaves[:])
    temp = list() #deve existir melhor maneira de limpar a lista
    temp_chaves = list()

for indice, linha in enumerate(numeroEuromillions):
    if indice % 2 == 0:
        for numero in linha:
            print(f' {numero} |', end = '')
    else:
        for numero in linha:
            print(f' *{numero} |', end = '')
        print()

