turma = []
qtd_alunos = 5

for c in range(qtd_alunos):
    aluno = dict()

    aluno['Nome'] = input(f'Digite o nome do {c+1}º aluno: ')
    aluno['Média'] = float(input(f'Digite a média do {aluno["Nome"]}: '))
    aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 9.5 else 'Reprovado'  # operador ternário

    turma.append(aluno)

for a in turma:
    print(f'O aluno(a) {a["Nome"]} teve média de {a["Média"]} e está {a["Situação"]}')