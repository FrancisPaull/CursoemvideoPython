'''
Faça um pg que leia um número de 0 a 9999 e mostre cada um dos digitos separados: unidade, dezena, centena, milhar.
'''

n = int(input('Digite um número: '))
uidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(u, d, c, m)
