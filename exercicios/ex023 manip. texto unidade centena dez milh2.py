'''
Faça um pg que leia um número de 0 a 9999 e mostre cada um dos digitos separados: unidade, dezena, centena, milhar.
'''

n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(u, d, c, m)
