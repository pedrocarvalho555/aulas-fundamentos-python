resposta = ''

print('O céu é azul?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V] / [F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou vamos à proxima')
    elif resposta == 'F':
        print('Errado, tente novamente')
    else:
        print('Resposta inválida')

print('O palmeiras tem mundial?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V] / [F]: ').strip().upper()
    if resposta == 'F':
        print('Acertou vamos à proxima')
    elif resposta == 'V':
        print('Errado, tente novamente')
    else:
        print('Resposta inválida')

print('O Ricardo é o nosso formador?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V] / [F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou vamos à proxima')
    elif resposta == 'F':
        print('Errado, tente novamente')
    else:
        print('Resposta inválida')


