velocidade_max = 80
print('--- Multatronix 2000 ---')
velocidade = int(input('---> '))

if velocidade > velocidade_max:
    multa = 100 + ((velocidade - velocidade_max) * 7)
    print(f'Portou-se mal, vai pagar {multa}€ de multa')
else:
    print('Boa viagem, o melhor presente é estar presente')
