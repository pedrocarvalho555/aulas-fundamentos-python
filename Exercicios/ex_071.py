def header(txt):
    tamanho = len(txt)
    print('-'*(30+tamanho))
    print(f'{txt:-^{30+tamanho}}') #nao acredito que funcionou
    print('-'*(30+tamanho))

texto = input('Digite a sua mensagem: ')
header(texto)