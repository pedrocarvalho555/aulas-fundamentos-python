primo = 0
numero = int(input('Digite um número de 1 a 1000: '))

for c in range (0, 1001): #executa o ciclo de 1-1000 para remover todos os numeros divisiveis por 2,3,5 excluindo os mesmos
    if c % 2 == 0:
        if 2 == numero:
            primo = 1
    elif c % 3 == 0:
        if 3 == numero:
            primo = 1
    elif c % 5 == 0:
        if 5 == numero:
            primo = 1
    elif c % numero == 0:
        primo = 1

if primo == 1:
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo')

