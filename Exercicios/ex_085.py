import urllib.request # biblioteca standard, existe o urllib.errors para tratar os erros, mas não achei necessário incluir

try:
    address = input('Digite o site e eu te direi se está online ou não (ex: www.iefp.pt)\n--> ')
    completa_https = 'https://'+address # o request precisa do https://, eu faço isso pelo utilizador.
    urllib.request.urlopen(completa_https)
except:
    print(f'O site {completa_https} não está online')
else:
    print(f'O site {completa_https} está online')

