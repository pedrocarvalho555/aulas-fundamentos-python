def header (txt: str) -> None:
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def menu_calculadora() -> None:
    header('CALCULADORA')
    print('[ 1 ] - Soma')
    print('[ 2 ] - Subtração')
    print('[ 3 ] - Multiplicação')
    print('[ 4 ] - Divisão')
    print('[ 5 ] - Menu Principal')
    option = int(input('---> '))

    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            main_menu()

def main_menu() -> None:
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
                pass
            case 2:
                header('TABUADA')
                pass
            case 3:
                header('PAR OU ÍMPAR')
                pass
            case 4:
                header('NÚMEROS PRIMOS')
                pass
            case 5:
                header('FATORIAL')
                pass
            case 6:
                print('A sair...')
                break