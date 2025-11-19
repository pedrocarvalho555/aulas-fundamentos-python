'''frase_dirty = input('Digite uma frase para verificarmos se é um palíndromo\n--> ').strip().lower()
frase_clean = frase_dirty.replace(' ', '')
length = len(frase_clean)
reverse = frase_clean[::-1]
print(f'{reverse}')

if reverse == frase_clean:
    print(f'{frase_clean} é palíndromo - {reverse}')
else:
    print(f'{frase_clean} não é palíndromo - {reverse}')'''

# ou

frase_dirty = input('Digite uma frase para verificarmos se é um palíndromo\n--> ').strip().lower()
frase_clean = frase_dirty.replace(' ', '')
length = len(frase_clean)
reverse = ''

for c in range (length, 0, -1):
    reverse = reverse + frase_clean[c-1]
if reverse == frase_clean:
    print(f'{frase_clean} é palíndromo - {reverse}')
else:
    print(f'{frase_clean} não é palíndromo - {reverse}')