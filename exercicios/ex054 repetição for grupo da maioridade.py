'''Crie um pg que leia a idade de 7 pessoas. no final mostre quantas pessoas são maiores de idade e quantas são menores.'''
from datetime import date
maior = 0
menor = 0
ano = date.today().year
for lista in range(1,8):
    nasc = int(input('Digite seu ano de nascimento da {}ª pessoa: '.format(lista)))
    if ano - nasc >= 18:
        maior += 1
    else:
        menor +=1
print('{} Pessoas são maiores de idade e {} são menores.'.format(maior, menor))