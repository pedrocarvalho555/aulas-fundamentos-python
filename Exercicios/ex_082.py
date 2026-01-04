'''
Crie um sistema que utilize o
interactive help do python. O utilizador
deve digitar o comando e o sistema deve
retornar o manual. Quando o utilizador
digitar “FIM” o programa deve encerrar.
'''

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def ajuda(txt: str):
        help(txt)

header('EXERCÍCIO 82')
while True:
    user_in = input('Digite o nome de uma função do python: ').lower().strip()
    if user_in == 'sair':
        break
    else:
        ajuda(user_in)