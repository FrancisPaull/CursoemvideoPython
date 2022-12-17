'''
Faça um pg que leia 3 números e mostre qual é maior
'''
menor = 0
maior = 1
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
n3 = int(input('Digite terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
    print('{} é o maior e {} é o menor'.format(maior, menor))
elif n2 > n1 and n2> n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
    print('{} é o maior e {} é o menor.'.format(maior, menor))
elif n3 > n1 and n3 > n2:
    maior = n3
    if n2 > n1:
        menor = n1
    else:
        menor = n2
    print('{} é o maior e {} é o menor'.format(maior, menor))