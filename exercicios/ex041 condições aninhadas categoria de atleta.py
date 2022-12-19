'''
A confederação nacional de natação precisa de um prograna que leia o ano de nascimento de um atleta e mostre sua categoria
de acordo com a idade:
Ate 9 anos - mirim
até 14 anos ifantil
até 19 anos junior
até 20 anos senior
acima de 20 anos master
'''
from datetime import date
nascimento = int(input('Digite seu ano de nascemento: '))
idade = date.today().year - nascimento
if idade < 9:
    print('Sua categoria é mirim.')
elif idade < 14:
    print('Sua categoria é infantil')
elif idade < 19:
    print('Sua categoria é junior.')
elif idade < 20:
    print('Sua categoria é senior.')
else:
    print('Sua categoria é master.')
print(idade)