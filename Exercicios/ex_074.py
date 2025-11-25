def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def sistema_notas(nome,lista):
    c = 0
    soma = 0
    media = 0
    for valor in lista:
        soma = soma + valor
        c+=1
    media = soma/c

    if media >= 9.5:
        print(f'O aluno(a) {nome} encontra-se aprovado com média de {media}')
    else:
        print(f'O aluno(a) {nome} encontra-se reprovado com média de {media}')

# main
lista_notas = list()

header('Avaliação')
nome = input('Digite o nome do aluno: ')

while True:
    nota = int(input('Digite a nota do aluno, digite -1 caso queira sair\n--> '))
    if nota < 0: #afinal pode ser qualquer valor negativo
        break
    else:
        lista_notas.append(nota)

sistema_notas(nome,lista_notas)

