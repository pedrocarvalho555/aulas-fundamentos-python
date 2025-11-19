print(' --- ESCOLA EB2/3 CURRAL DE MOINAS ---')
nota1 = float(input('Insira a primeira nota do aluno --> '))
nota2 = float(input('Insira a segunda nota do aluno --> '))
nota3 = float(input('Insira a terceira nota do aluno --> '))
nota4 = float(input('Insira a quarta nota do aluno --> '))
nota5 = float(input('Insira a quinta nota do aluno --> '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 9.5:
    print(f'Passou com média de ({media})')
elif media > 8 and media < 9.5:
    print(f'Em recuperação com média de ({media})')
else:
    print(f'Reprovado com média de ({media}')