#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo valor com 15%de aumento.

preco = int(input('Digite um valor: '))
desconto = int(input('Digite o valor do desconto: '))
vldesconto = (preco / 100) * desconto
total = preco + vldesconto
print('total é {}.'.format(total))


