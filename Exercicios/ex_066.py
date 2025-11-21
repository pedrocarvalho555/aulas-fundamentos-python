'''

Crie um simulador de crédito habitação
simples e sem taxas, que solicite o nome,
ano de nascimento, rendimentos mensais,
despesas mensais, montante do crédito e
prazo em anos, guardando tudo dentro de um
dicionário. Calcule, acrescentando ao
dicionário, a idade, o remanescente após
despesas, quanto deverá pagar mensalmente
pelo crédito e se o crédito foi aprovado
sempre que o remanescente seja superior ao
valor mensal do crédito.

'''
from time import sleep

pedinte = dict()

print('--- SIMULADOR DE CRÉDITO ---')

pedinte["Nome"] = input('Qual o seu nome?\n--> ')
pedinte["AnoNasc"] = int(input('Em que ano nasceu?\n--> '))
pedinte["Idade"] = 2025 - pedinte["AnoNasc"] #estou ciente que existe uma biblioteca para ir buscar o ano atual
pedinte["Rendimento"] = int(input('Qual é o seu rendimento mensal?\n--> '))
pedinte["Despesa"] = int(input('E quais são as suas despesas mensais?\n--> '))
pedinte["RendaLiquida"] = pedinte["Rendimento"] - pedinte["Despesa"]
pedinte["Credito"] = int(input('Qual é o valor do seu crédito?\n--> '))
pedinte["DuracaoCredito"] = int(input('Qual é o prazo do seu crédito em meses relembrando que cada ano tem 12 meses\n--> '))
pedinte["PagamentoMensal"] = pedinte["Credito"] / pedinte["DuracaoCredito"]

if pedinte["PagamentoMensal"] < pedinte["RendaLiquida"]:
    pedinte["Aprovacao"] = 'Aprovado'
else:
    pedinte["Aprovacao"] = 'Reprovado'

print('A calcular o seu crédito.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(2)

print(f'Utilizador: {pedinte["Nome"]}')
print(f'Ano Nascimento: {pedinte["AnoNasc"]} - {pedinte["Idade"]} anos')
print(f'Rendimento: {pedinte["Rendimento"]} | Despesa: {pedinte["Despesa"]} | Renda Liquida: {pedinte["RendaLiquida"]}')
print(f'Credito: {pedinte["Credito"]} com duração de {pedinte["DuracaoCredito"]} meses')
print(f'Pagamento Mensal: {pedinte["PagamentoMensal"]}')
print(f'O seu crédito encontra-se {pedinte["Aprovacao"]}')