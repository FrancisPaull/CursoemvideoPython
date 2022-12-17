'''
Faça um pg que leia 3 números e diga ao usuário se podem ou não formar um triângulo.
'''

# se a soma da medida de 2 retas for maior que a terceira é possível formar um triângulo.

r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida  da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível construir um triângulo com essas retas!')
else:
    print('Não é possível construir um triângulo.')