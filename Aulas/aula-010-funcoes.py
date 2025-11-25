def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def soma():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(f'{num1} + {num2} = {num1+num2}')

def subtracao():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(f'{num1} - {num2} = {num1-num2}')


def multiplicacao():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(f'{num1} x {num2} = {num1 * num2}')


def divisao():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(f'{num1} / {num2} = {num1 / num2}')

def menu_calc():
    while True:
        header('CALCULADORA')
        print('[ 1 ] - Soma')
        print('[ 2 ] - Subtracao')
        print('[ 3 ] - Multiplicacao')
        print('[ 4 ] - Divisao')
        opcao = int(input('---> '))

        if opcao == 1:
            header('SOMA')
            soma()
        elif opcao == 2:
            header('SUBTRAÇÃO')
            subtracao()
        elif opcao == 3:
            header('MULTIPLICAÇÃO')
            multiplicacao()
        elif opcao == 4:
            header('DIVISÃO')
            divisao()
        else:
            print('A sair...')
            break
#########################################
#Programa principal

menu_calc()