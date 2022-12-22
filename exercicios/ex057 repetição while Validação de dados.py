'''Faça um pg que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. '''

sexo = input('Digite seu sexo [M/F]: ').upper()

while sexo not in 'MF':
    sexo = str(input('Valor inválido.Digite novemente: ')).upper()

print('Sexo registrado.')