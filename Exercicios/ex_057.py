lista = []
while True:
    insert = int(input('Digite um número, digite numero negativo para sair: '))
    if insert < 0:
        break
    if lista.count(insert) == 0:
        lista.append(insert)
    else:
        print('Número já existe na lista, não será adicionado')

lista.sort(reverse=True)

for c in range(len(lista)): # esqueci-me como fazer um foreach
    print(lista[c])