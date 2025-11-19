aluno1 = ['Telmo', 14]
aluno2 = ['Solinho', 17]
aluno3 = ['Pedro', 16]
aluno4 = ['Leticia', 15]

turma = list()

turma.append(aluno1[:]) #se nao tiver o [:] vai buscar a variavel/endereço de memória e não apenas o valor que está la
turma.append(aluno2) #tornando-se assim "dinamico" por assim dizer
turma.append(aluno3)
turma.append(aluno4)

print(turma)

aluno1[0] = 'Alexandra'
aluno1[1] = 18

for aluno in turma:
    print(f'O aluno no índice {aluno[0]} tem uma média de {aluno[1]} valores.')
