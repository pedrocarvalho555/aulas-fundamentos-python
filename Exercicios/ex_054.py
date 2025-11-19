tuple = (int(input('Digite o primeiro valor: ')),
         int(input('Digite o segundo valor: ')),
         int(input('Digite o terceiro valor: ')),
         int(input('Digite o quarto valor: '))) # tuple com input do utilizador

c_sete = 0 # quantidade de 7's
c_indice = 0 # indice porque quis utilizar foreach
c_par = 0 # contador de pares
c_cinco = 0

for valor in tuple:
    if valor == 7:
        c_sete+=1
    elif valor == 5:
        print(f'O 5 está na posição {c_indice}')
        c_cinco+=1
    elif valor % 2 == 0:
        print(f'O valor {valor} na posição {c_indice} é par')
        c_par+=1
    c_indice+=1

if c_sete == 0 and c_par == 0 and c_cinco == 0: #verificação final porque eu percebi mal o exercicio e pensei que era só para mostrar erro case nenhum caso fosse positivo.
    print('Nenhuma condição atingida')
else:
    if c_sete == 0:
        print('Nenhum 7 encontrado')
    else:
        print(f'Existe {c_sete} número/s com o valor de 7')

    if c_par == 0:
        print('Nenhum número par')
    if c_cinco == 0:
        print('Nenhum 5 encontrado')