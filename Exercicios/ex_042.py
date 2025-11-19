# opcional - mostrar se é mais acima ou mais abaixo
from random import randint

aleatorio = randint(0, 10)
tentativas = 0

print(' --- Adivinhe o número --- ')
print(' --- Receba um prémio --- ')
print('Digite um número de 0 a 10')
while True:
    numero_input = int(input('--> '))
    if aleatorio == numero_input:
        tentativas+=1
        print(' *** GANHOU *** ')
        print(f'Acertou com {tentativas} tentativas')
        break
    elif numero_input > 10:
        print('Número inválido, tente novamente')
    else:
        if aleatorio > numero_input:
            print('Errado, o número é maior, tente novamente')
            tentativas+=1
        else:
            print('Errado, o número é menor, tente novamente')
            tentativas+=1