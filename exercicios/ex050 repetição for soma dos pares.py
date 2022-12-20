'''Crie um pg que leia seis números inteiros e mostre a soma apenas dos que forem pares '''
soma = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 ==0:
        soma += n
print('O resulta da soma dos números pares digitados é {}.'.format(soma))