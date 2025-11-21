'''

Crie um programa que leia o nome, sexo e
idade de várias pessoas, guardando cada
dado num dicionário e todos os
dicionários numa lista. No final mostre:

a) Quantas pessoas foram registadas;
b) Qual a média de idades do grupo;
c) Quantas mulheres foram registadas;
d) Quantos homens com idade acima da média foram
registados.

'''
lista = list()
c_pessoas = 0
c_mulheres = 0
c_homensAcimaMedia = 0
soma_idade = 0
media = 0
escape = ''

print('--- CENSOS CURRAL DE MOINAS 2033 ---')
while True:
    pessoas = dict()
    print('Vamos começar o registo para os censos, para sair digite "0" no campo do nome')
    escape = input('Digite o nome: ')
    if escape == '0':
        break
    else:
        pessoas["Nome"] = escape
        c_pessoas += 1
    pessoas["Genero"] = input('Qual o género da pessoa (M/F): ').capitalize()
    if pessoas["Genero"] == 'F':
        c_mulheres += 1
    pessoas["Idade"] = int(input('Qual a idade: '))
    lista.append(pessoas)

c = 0
while c < c_pessoas:
    soma_idade = lista[c]["Idade"] + soma_idade
    c+=1
media = soma_idade / c_pessoas

b = 0
while b < c_pessoas:
    if lista[b]["Genero"] == 'M' and (lista[b]["Idade"] > media):
        c_homensAcimaMedia +=1
    b+=1

print(f'Foram registas {c_pessoas} pessoas')
print(f'Dessas pessoas {c_mulheres} são mulheres')
print(f'A média de idades é {media}')
print(f'E {c_homensAcimaMedia} homens têm idade acima da média')