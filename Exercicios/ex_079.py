'''
Crie um programa com uma função que vai
funcionar como a função input(), no
entanto vai fazer a validação para
aceitar apenas um valor numérico.
'''

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def check_type():
    user_in = input('Digite apenas valores numéricos: ')
    if user_in.isnumeric():
        print('Realmente, é um valor numérico')
    else:
        print('Valor invalido')

header('EXERCICIO 079')
check_type()