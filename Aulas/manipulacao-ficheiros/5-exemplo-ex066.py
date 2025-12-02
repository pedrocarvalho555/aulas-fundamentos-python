from time import sleep
from pathlib import Path
from datetime import datetime

source=Path('files/dados.txt')

def cabecalho(txt: str) -> None:
    print(f'---{txt.upper()}---')

def busca_informacao() -> dict:
    dados = dict()
    with source.open('r', encoding='utf-8', errors='ignore') as file:
        for linha in file:
            # linha = linha.replace('\n', '') # limpa o \n
            linha_dividida = linha.split(': ')
            # linha_limpa = linha_dividida
            dados[linha_dividida[0]] = linha_dividida[1].replace('\n', '')

    return dados

def calcula_informacao(dados: dict) -> dict:

    ano_atual = datetime.now().year

    dados["Idade"] = ano_atual - int(dados["AnoNasc"])
    dados["RendaLiquida"] = float(dados["Rendimento"]) - float(dados["Despesa"])
    dados["Credito"] = float(input('Qual é o valor do seu crédito?\n--> '))
    dados["DuracaoCredito"] = int(input('Qual é o prazo do seu crédito em meses relembrando que cada ano tem 12 meses\n--> '))
    dados["PagamentoMensal"] = int(dados["Credito"]) / int(dados["DuracaoCredito"])

    if dados["PagamentoMensal"] < dados["RendaLiquida"]:
        dados["Aprovacao"] = 'Aprovado'
    else:
        dados["Aprovacao"] = 'Reprovado'

 # printa logo tudo

    print('A calcular o seu crédito', end='')
    for c in range(3):
        sleep(1)
        print('.', end='')

    print(f'\nUtilizador: {dados["Nome"]}')
    print(f'Ano Nascimento: {dados["AnoNasc"]} - {dados["Idade"]} anos')
    print(f'Rendimento: {dados["Rendimento"]} | Despesa: {dados["Despesa"]} | Renda Liquida: {dados["RendaLiquida"]}')
    print(f'Credito: {dados["Credito"]} com duração de {dados["DuracaoCredito"]} meses')
    print(f'Pagamento Mensal: {dados["PagamentoMensal"]}')
    print(f'O seu crédito encontra-se {dados["Aprovacao"]}')

def guarda(dados: dict) -> str:
    caminho = Path(rf'files/{dados["Nome"]}resultados.txt')
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        for key, values in dados.items():
            file.write(f'{key}: {value}\n')

    return f'Resultado de {dados["Nome"]} guardado com sucesso.'

print(guarda()) # tbd
pessoa = calcula_informacao(busca_informacao())
