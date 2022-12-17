'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um PG que leia os quatro nomes e mostre a ordem sorteada'''

import random

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'A ordem será {lista}.')

