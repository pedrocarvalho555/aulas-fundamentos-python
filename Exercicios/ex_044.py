numero = int(input('Digite um número: '))
controlo = numero-1
fatorial = 1

while controlo != 0:
    print(f'{numero} x {numero-controlo} + {fatorial}')
    fatorial = (fatorial*(numero-controlo)) + fatorial
    controlo-=1

print(f'O fatorial de {numero} é {fatorial}')