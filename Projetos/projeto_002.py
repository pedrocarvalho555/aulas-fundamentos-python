#Pedro, Luanna, Julia, Elionai
import time

print(' --- [BOAS VINDAS] --- \n')
time.sleep(1)

print('Faça o seu registo')
username_in = input('Username: ').strip()
email_in = input('Email: ').strip()

#Verifica se é email
if email_in.count('@') == 0 and email_in.count('.') == 0:
    print('Email inválido, digite novamente')
    email_in = input('Email: ').strip()

password_in = input('Password: ').strip()
#Verifica se a password é igual ao username
if username_in == password_in:
    print('A password não pode ser igual ao username')
    password_in = input('Password: ').strip()

time.sleep(0.5)
print('Criando o seu perfil', end='')
time.sleep(0.5)
print('.', end='')
time.sleep(0.5)
print('.', end='')
time.sleep(0.5)
print('.')
time.sleep(1)
print('Registo efetuado com sucesso, vamos reencaminhar para o login\n')
time.sleep(1)

print(' --- [MENU] --- ')
print('[1] - Login')
print('[2] - Sair')
opcao = input('--> ').strip().lower()

if opcao == 'login' or opcao == '1':
    print(' --- [BEM VINDO] --- ')
    username = input('Username: ').strip()
    email = input('Email: ').strip()
    password = input('Password: ').strip()
    if username == username_in and email == email_in and password == password_in:
        print(f'Login efetuado com sucesso.\nBem Vindo {username}')
    else:
        print('Username, password ou email errado, tente novamente')
        username = input('Username: ').strip()
        email = input('Email: ').strip()
        password = input('Password: ').strip()
        if username == username_in and email == email_in and password == password_in:
            print(f'Login efetuado com sucesso.\nBem Vindo {username}')
        else:
            print('Username, password ou email errado novamente, conta bloqueada')

elif opcao == 'sair' or opcao == '2':
    print('Obrigado por utilizar o nosso programa, tenha um bom dia')
else:
    print('Opção inválida')

