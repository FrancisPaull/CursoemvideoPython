'''Crie um pg que leia o peso de cinco pessoas e mostre qual foi o maior e qual foi o menor peso.'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior, menor)