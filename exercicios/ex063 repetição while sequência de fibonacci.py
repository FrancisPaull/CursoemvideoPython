'''Escreva um pg que leia um número inteiro e mostre na tela os n primeiros elementos de uma sequencia de fibonacci'''


termos = int(input('Quantos termos da sequencia de fibo gostaria de mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}' .format(t1, t2, end=''))
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print('Fim')