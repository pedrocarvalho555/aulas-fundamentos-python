print('--- Calculadora ---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Números Pares')
print('[ 4 ] – Sair')
option_main = int(input('-->'))

if option_main == 1:
    print('Escolheu Tabuada')
    valor = int(input('Insira um valor numérico para podermos calcular a tabuada\n-->'))
    print(f'{valor} x 1 = {valor * 1}')
    print(f'{valor} x 2 = {valor * 2}')
    print(f'{valor} x 3 = {valor * 3}')
    print(f'{valor} x 4 = {valor * 4}')
    print(f'{valor} x 5 = {valor * 5}')
    print(f'{valor} x 6 = {valor * 6}')
    print(f'{valor} x 7 = {valor * 7}')
    print(f'{valor} x 8 = {valor * 8}')
    print(f'{valor} x 9 = {valor * 9}')
    print(f'{valor} x 10 = {valor * 10}')

elif option_main == 2:
    print('O que deseja calcular?')
    print('[ 1 ] - SOMA')
    print('[ 2 ] - SUBTRAÇÃO')
    print('[ 3 ] - DIVISÃO')
    print('[ 4 ] - MULTIPLICAÇÃO')
    option_calculadora = int(input('-->'))
    if option_calculadora == 1:
        print('Escolheu SOMA')
        soma1 = int(input('Digite um número: '))
        soma2 = int(input('Digite outro número: '))
        print(f'O resultado da soma é {soma1 + soma2}')

    elif option_calculadora == 2:
        print('Escolheu SUBTRAÇÃO')
        subtracao1 = int(input('Digite um número: '))
        subtracao2 = int(input('Digite outro número: '))
        print(f'O resultado da subtração é {subtracao1 - subtracao2}')

    elif option_calculadora == 3:
        print('Escolheu DIVISÃO')
        divisao1 = int(input('Digite um número: '))
        divisao2 = int(input('Digite outro número: '))
        print(f'O resultado da subtração é {divisao1 / divisao2}')

    elif option_calculadora == 4:
        print('Escolheu MULTIPLICAÇÃO')
        multiplicacao1 = int(input('Digite um número: '))
        multiplicacao2 = int(input('Digite outro número: '))
        print(f'O resultado da subtração é {multiplicacao1 * multiplicacao2}')

    else:
        print('Opção inválida, o programa irá encerrar')

elif option_main == 3:
    print('Números Pares')
    numero = int(input('Digite um número\n--> '))

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')

elif option_main == 4:
    print('O programa irá encerrar')

else:
    print('Opção não reconhecida, erro')
