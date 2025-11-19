import random

print(' --- [PEDRA | PAPEL | TESOURA] ---')
escolha = input('Pedra papel ou tesoura?\n-->').upper().strip
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
npc_escolha = random.choice(opcoes)
print(f'O seu adversário escolheu {npc_escolha} e você escolheu {escolha}')

if escolha == npc_escolha:
    print('EMPATOU')

elif escolha == 'PEDRA' and npc_escolha == 'TESOURA':
    print('GANHOU')

elif escolha == 'TESOURA' and npc_escolha == 'PAPEL':
    print('GANHOU')

elif escolha == 'PAPEL' and npc_escolha == 'TESOURA':
    print('GANHOU')

else:
    print('PERDEU')