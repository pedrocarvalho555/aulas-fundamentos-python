numeros = list()

for linha in range (0,3):
    temp = list()

    for coluna in range (0,3):
        num = int(input('Digite um número: '))
        temp.append(num)

    numeros.append(temp[:])

for lista in numeros:
    for valor in lista:
        print(valor, end=' ')
    print()