#Faça um programa que leia um número inteiro e mostre na tela seu antecessor e sucessor.

n1 = int(input('Digite um número:'))
ant = n1 - 1
suc = n1 + 1
print('O número {}, têm {} como antecessor e {} como sucessor.'.format(n1,ant,suc))

