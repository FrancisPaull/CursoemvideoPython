"""__________________ __________________ __________________ __________________ __________________
Crie um pg que leia, NOME, Ano de NASCIMENTO, e carteira de trabalho e cadastre-os com idade em um dicionário,
SE o numéro da carteira de trabalho for diferente de zero. O dicionário receberá tambérm o ano de contratação e
o salário. Calcule e acresente além da idade, com quantos anos a pessoa vai se aposentar.
__________________ __________________ __________________ __________________ __________________"""
from datetime import datetime
cadastro = {}
cadastro['Nome'] = input('Digite seu nome: ')
idade = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - idade
cttps = int(input('Número da carteira de trabalho: '))
if cttps != 0:
    cadastro['Cttps'] = cttps
    cadastro['Ano de contratação:'] = int(input('Qual o ano de contratação: '))
    cadastro['Salário'] = int(input('Qual valor do salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Ano de contratação:'] + 35) - datetime.now().year)
for k, v in cadastro.items():
    print(f'{k}: {v}.')