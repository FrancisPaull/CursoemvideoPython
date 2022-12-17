'''
Crie um pg que leia um numero inteiro e diga se é par ou ímpar.
'''

numero = int(input('Digite um número: '))
if numero % 2 == 1:
    print('{} é ímpar!'.format(numero))
else:
    print('{} é par.'.format(numero))