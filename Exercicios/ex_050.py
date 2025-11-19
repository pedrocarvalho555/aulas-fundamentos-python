print('Registo de utilizadores')
contador_H17menos = 0
contador_25plus = 0
contador_mulheres = 0
contador_menores = 0
while True:
    genero = input('Digite o género [M/F]: ').strip().upper()
    if genero != 'M' and genero != 'F':
        print('Inválido, tente novamente')
    else:
        idade = int(input('Digite a idade: '))
        if idade > 25:
            contador_25plus += 1
        if idade < 18:
            contador_menores += 1
        if genero == 'F':
            contador_mulheres+=1
        if genero == 'M' and idade < 17:
            contador_H17menos+=1
        opcao = input('Deseja continuar depois deste registo? [S/N] \n-->').strip().upper()
        if opcao == 'N':
            print('Compreendido, iremos encerrar o registo.')
            break

print(f'Existem {contador_H17menos} homens com menos de 17 anos')
print(f'Existem {contador_25plus} pessoas com mais de 25 anos')
print(f'Existem {contador_mulheres} mulheres')
print(f'Existem {contador_menores} menores de idade')