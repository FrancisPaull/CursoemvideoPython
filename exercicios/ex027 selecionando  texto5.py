'''
Faça um pg que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.
'''

nome = str(input('Digite seu nome completo')).strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
nome = nome.