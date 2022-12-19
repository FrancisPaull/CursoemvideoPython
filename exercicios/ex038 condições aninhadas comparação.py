'''
Escreva um pg que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
--o primeiro valor é maior
--o segundo valor é maior
--os número são iguais
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('{} e {} são iguais.')