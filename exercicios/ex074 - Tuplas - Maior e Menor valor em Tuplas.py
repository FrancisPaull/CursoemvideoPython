"""___________________ ___________________ ___________________ ___________________ ___________________
Crie um pg que vai gerar cinco nume aleatórios e coloqueos em uma tupla. Depois disso
mostre a listagem de números gerados e indique o menor e maior valor gerado na tupla.
___________________ ___________________ ___________________ ___________________ ___________________ """

from random import randint
n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os números sorteados são: {n}')
print(f'O menor valor na lista é {max(n)}.')
print(f'O maior valor na Lista é {min(n)}.')
