#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = int(input('Digite um valor: '))
n2 = float(input('Qual valor do dolar no cambio atual: '))
dol = n1 / n2
print('Com {} reais você consegue comprar {:.2f} dolares.'.format(n1,dol))

