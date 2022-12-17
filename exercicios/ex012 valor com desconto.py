#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = int(input('Digite o valor: '))
novo = (valor / 100) * 5
desc = valor - novo
print(f'Novo valor é {desc} reais.')


