from math import factorial

def soma () -> None:
    '''
    Soma de dois número
    '''

    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(f'{num1} + {num2} = {num1+num2}')

    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def subtracao () -> None:
    '''
    Subtração de dois número
    '''
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(f'{num1} - {num2} = {num1-num2}')

    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def multiplicacao () -> None:
    '''
    Multiplicação de dois número
    '''
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(f'{num1} x {num2} = {num1*num2}')

    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def divisao () -> None:
    '''
    Divisão de dois número
    '''
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(f'{num1} / {num2} = {num1/num2}')

    except ValueError:
        print('Por favor digite um número válido.')

    except ZeroDivisionError:
        print('Não é possível dividir por zero.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def tabuada () -> None:
    '''
    Tabuada de um número inteiro digitado pelo utilizador
    '''
    try:
        num1 = int(input('Digite um número: '))
        for c in range (1, 11):
            print(f'{num1} x {c} = {num1*c}')
    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def par_impar () -> None:
    '''
    Verifica se o número inserido pelo utilizador é par ou ímpar
    '''
    try:
        num1 = int(input('Digite um número: '))
        if num1 % 2 == 0:
            print(f'O número {num1} é par')
        else:
            print(f'O número {num1} é ímpar')
    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')

def primos() -> None:
    '''
    Verifica se o número inserido pelo utilizador é primo
    '''
    primo = 0
    numero = int(input('Digite um número de 1 a 1000: ')) #fui buscar a um exercicio mais antigo, de certeza que já fizemos melhor

    for c in range(0,
                   1001):  # executa o ciclo de 1-1000 para remover todos os numeros divisiveis por 2,3,5 excluindo os mesmos
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


def fatorial () -> None:
    '''
    Utiliza a livraria math para efetuar o calculo do fatorial de um número inserido pelo utilizador
    '''
    try:
        num1 = int(input('Digite um numero para calcularmos o fatorial: '))
        print(f'O fatorial de {num1} é :{factorial(num1)}')

    except ValueError:
        print('Por favor digite um número válido.')

    except KeyboardInterrupt:
        print('O utilizador encerrou o programa.')
