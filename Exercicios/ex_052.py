la_liga = ('Real Madrid', 'FC Barcelona', 'Vilarreal FC', 'Bétis', 'Atlético Madrid',
           'Sevilha FC', 'Elche CF', 'Atl. Bilbao', 'RCD Espanhol de Barcelona', 'Deportivo Alavés',
           'Getafe FC', 'CA Osasuna', 'Levante UD', 'Rayo', 'Valencia CF' ,'RC Celta de Vigo', 'Real Oviedo FC',
           'Girona FC', 'Real Sociedad', 'RCD Mallorca')
MUNDIAL_PALMEIRAS = 0 #importante

print('PRIMEIROS CLASSIFICADOS')
for c in range (0, 5):
    print(f'{c+1}º - {la_liga[c]}')

print('\nÚLTIMOS CLASSIFICADOS')
for c in range (16, 20):
    print(f'{c+1}º - {la_liga[c]}')

print('\nPOR ORDEM ALFABÉTICA')
for equipa in sorted(la_liga):
    print(f'\t{equipa}')
print() # só um paragrafo pra ficar mais bonito

for clube in la_liga: # verifica se o las palmas existe no tuple
    if clube != 'Las Palmas':
        MUNDIAL_PALMEIRAS = 0
    else:
        MUNDIAL_PALMEIRAS = 1
        break

if MUNDIAL_PALMEIRAS == 0:
    print('Las Palmas está igual ao mundial do Palmeiras')
else:
    for c in range(0, len(la_liga)): # dava para fazer esta verificação mais acima.
        if la_liga[c] == 'Las Palmas':
            print(f'{c}º - {la_liga[c]}')

