'''Faça um Pg que leia um número e diga se ele é ou não número primo. '''

n = int(input('Digite um número: '))
primeiro = 0
contador = 0
for c in range(primeiro, n):
    primeiro += 1
    if n % primeiro == 0:
        contador += 1
if contador == 2:
    print('{} é um número primo: '.format(n))
else:
    print('{} não é um número primo.'.format(n))


