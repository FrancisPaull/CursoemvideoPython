'''Crie um pg que leia varios números inteiros e só pare quando o número 999 for digitado, no final mostre quantos
números foram digitados e qual a soma entre eles desconsiderando o flag'''
n=0
soma = 0
flag = 999
cont = 0
while n != flag:
    n = int(input('"digite um número: '))
    if n != 999:
        soma += n
        cont += 1
print('Você digitou {} números, a soma entre eles é {}.'.format(cont, soma))
print('Fim')