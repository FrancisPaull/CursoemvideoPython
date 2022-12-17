'''
Crie um pg que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
'''

nome = str(input('Digite seu nome: ')).upper().strip()
print(nome[:6] == 'SILVA' )