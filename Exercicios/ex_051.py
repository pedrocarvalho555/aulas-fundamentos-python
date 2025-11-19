extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Catorze', 'Quinze', 'Dezasseis', 'Dezassete', 'Dezoito',
           'Dezanove', 'Vinte')

while True:
    user_in = int(input('Digite um número de 0 a 20: '))
    if user_in < 0 or user_in > 20:
        print('Input inválido, tente novamente.')
    else:
        print(f'O seu número é {extenso[user_in]}')
        break