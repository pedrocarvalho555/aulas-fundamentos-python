valor1 = int(input('Digite o 1º número: '))
valor_maior = valor1
valor_menor = valor1
valor2 = int(input('Digite o 2º número: '))
if valor2 > valor_maior:
    valor_maior = valor2
elif valor2 < valor_maior:
    valor_menor = valor2
valor3 = int(input('Digite o 3º número: '))
if valor3 > valor_maior:
    valor_maior = valor3
elif valor3 < valor_menor:
    valor_menor = valor3


while True:
    print('\n --- CALCUCATRONIX ---')
    print('[1] SOMA')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opcao = int(input('--> '))
    if opcao == 1:
       print(f'{valor1} + {valor2} + {valor3} = {valor1+valor2+valor3}')
    elif opcao == 2:
       print(f'{valor1} x {valor2} x {valor3} = {valor1*valor2*valor3}')
    elif opcao == 3:
       print(f'O maior número é {valor_maior} e o menor é {valor_menor}')
    elif opcao == 4:
       valor1 = int(input('Digite o 1º número: '))
       valor_maior = valor1
       valor_menor = valor1
       valor2 = int(input('Digite o 2º número: '))
       if valor2 > valor_maior:
           valor_maior = valor2
       elif valor2 < valor_maior:
           valor_menor = valor2
       valor3 = int(input('Digite o 3º número: '))
       if valor3 > valor_maior:
           valor_maior = valor3
       elif valor3 < valor_menor:
           valor_menor = valor3
    elif opcao == 5:
        print('A sair...')
        break
