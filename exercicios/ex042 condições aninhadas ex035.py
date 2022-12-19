'''
Faça um pg que leia 3 números e diga ao usuário se podem ou não formar um triângulo.
e informe se o triangulo que será formado é:
equilátero = todos os lados iguais
isóceles = dois lados iguais
escaleno = todos os lados diferentes
'''

r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida  da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível construir um triângulo com essas retas!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Esse triângulo é Equilátero.')
    elif r1 == r2 and r1 != r3:
        print('Esse triangulo é isóceles, pois tem 2 lados iguais')
    else:
        print('Esse triângulo é escaleno')

else:
    print('Não é possível construir um triângulo.')