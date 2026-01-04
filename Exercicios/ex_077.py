'''
Crie um programa que tenha uma função
que vai receber como parâmetro o ano de
nascimento de uma pessoa e que crie um
ficheiro que informe se a pessoa já pode
tirar a carta de condução, se precisa de
autorização do encarregado de educação
ou se não pode.

+18 anos – pode
-16 anos – não pode
-18 e +16 – com autorização
'''
from datetime import datetime
from pathlib import Path

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def verifica_idade(ano_nasc: int):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    path = Path(rf'files/ex_077.txt')

    if idade >= 18:
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write('Pode tirar a carta de condução')
    elif idade < 16:
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write('Não pode tirar a carta de condução')
    else:
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write('Pode tirar a carta de condução apenas com autorização do encarregado de educação')



header('CARTA DE CONDUÇÃO')
ano_nasc = int(input('Digite o ano de nascimento: '))
verifica_idade(ano_nasc)