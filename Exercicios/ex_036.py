from time import sleep

numero = int(input('Digite um número para podermos fazer a tabuada: '))
for c in range (0, 10):
    print(f'{numero} x {c+1} = {numero * (c+1)}')
    sleep(0.5)