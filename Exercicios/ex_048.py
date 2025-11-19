from time import sleep

while True:
    numero = int(input('Digite um número para podermos fazer a tabuada: '))
    if numero <= 0:
        print('A sair do programa')
        break
    else:
        for c in range (0, 10):
            print(f'{numero} x {c+1} = {numero * (c+1)}')
            sleep(0.3)
