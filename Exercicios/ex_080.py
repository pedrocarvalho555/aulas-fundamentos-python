'''
Crie um programa com uma função que vai
receber várias notas de alunos e vai
retornar um dicionário com o seguinte:

a) Quantidade de notas
b) A maior nota
c) A média da turma
d) A situação (lógico opcional)
>12 – boa
<9,5 – fraca
>9,5 e <12 - razoável
'''

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def alunos():
    turma = dict()
    maior = 0
    media = 0
    contador = 0
    while True:
        check = input('Digite "sair" para sair ou pressione enter para continuar: ').lower().strip()
        if check == 'sair':
            break
        else:
            contador += 1
            turma[f"nota{contador}"] = int(input('Digite a nota do aluno: '))
            if turma[f"nota{contador}"] < 9.5:
                turma[f"situacao{contador}"] = 'Fraco'
            elif turma[f"nota{contador}"] > 12:
                turma[f"situacao{contador}"] = 'Boa'
            else:
                turma[f"situacao{contador}"] = 'Razoavel'


    for c in range(1, contador): # adiciona tudo na média
        media += turma[f"nota{c}"]
        if turma[f"nota{c}"] > maior:
            maior = turma[f"nota{c}"]
    media = media / contador
    turma["contagem"] = contador
    turma["media"] = media
    turma["maior"] = maior
    print(turma)


header('EXERCICIO 079')
alunos()