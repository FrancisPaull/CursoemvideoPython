'''
Faça um pg que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é hora de se alistar
- Se já passou do tempo de se alistar.
O programa também deverá mostrar o tempo que faltante ou o tempo excedente.
'''
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
falta = (18 - idade) * 12
sobra = (idade - 18) *12
if idade == 18:
    print('Parabéns você já completou 18 anos. Já pode se alistar!')
elif idade < 18:
    print('Ainda não chegou sua hora, ainda faltam {} meses para você se alistar.'.format(falta))
elif idade > 18:
    print('Você está atrasado, já excedeu {} meses para o alistamento.'.format(sobra))
