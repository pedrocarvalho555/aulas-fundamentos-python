string = input('Digite o seu nome:\n-->').strip().title()
string_split = string.split()
print(f'Olá {string_split[0]} {string_split[-1]} o seu registo está completo')
dominio_empresa = '@empresa.com'
email = f'{string[0]}.{string_split[-1]}{dominio_empresa}'.lower()
print(f'O seu email é {email}')