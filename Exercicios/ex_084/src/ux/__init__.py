from ..calc import *

def header (txt: str) -> None:
    '''
    Cabeçalho genérico que utilizo em literamente tudo que é lado
    '''
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def menu_calculadora() -> None:
    '''
    Menu da calculadora
    '''
    header('CALCULADORA')
    print('[ 1 ] - Soma')
    print('[ 2 ] - Subtração')
    print('[ 3 ] - Multiplicação')
    print('[ 4 ] - Divisão')
    print('[ 5 ] - Menu Principal')
    option = int(input('---> '))

    match option:
        case 1:
            soma()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao()
        case 5:
            main_menu()

def main_menu() -> None:
    '''
    Menu principal
    '''
    while True:
        header('EXERCÍCIO 84')
        print('[ 1 ] - Calculadora')
        print('[ 2 ] - Tabuada')
        print('[ 3 ] - Par ou Ìmpar')
        print('[ 4 ] - Números primos')
        print('[ 5 ] - Fatorial')
        print('[ 6 ] - Sair')
        option = int(input('---> '))

        match option:
            case 1:
                header('CALCULADORA')
                menu_calculadora()
            case 2:
                header('TABUADA')
                tabuada()

            case 3:
                header('PAR OU ÍMPAR')
                par_impar()

            case 4:
                header('NÚMEROS PRIMOS')
                primos()
            case 5:
                header('FATORIAL')
                fatorial()
            case 6:
                print('A sair...')
                break