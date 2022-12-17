'''
Faça um pg que leia um ano e diga se ele é bissexto
'''

# Ano bissexto ocorre a cada 4 anos exceto em anos múltiplos de 100 que não são múltiplos de 400.
from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %  100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))