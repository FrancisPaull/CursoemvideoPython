'''
Crie um pg que leia o nome completo de uma pessoa e mostre:
    --O nome com todas as  letras maiúsculas
    --todas minúsculas
    --Quantas letras ao todos sem considerar os espaços.
    --quantas letras tem o primeiro nome

'''

nome = str(input('Digite seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
nome = nome.split()
print(len(nome[0]))