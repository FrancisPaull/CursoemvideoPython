'''______________________________________________________________________________________________________
Crie um pg que simule o funcionamento de um caixa eletrônico. no início pergunte ao usuário qual o valor a ser sacado
e o pg vai informar quantas cédulas de cada valor serão entregues.
Obs.: cedulas de 1, 10, 20 e 50
___________________________________________________________________________________________________________'''


valor = int(input('Qual o valor do saque ? '))
valortotal = valor
ced = 50
totalced = 0
while True:
    if valortotal >= ced:
        valortotal -= ced
        totalced +=1
    else:
        if valortotal != 0:
            print(f'Total de {totalced} cédulas de {ced} reais')
        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if valortotal == 0:
            break













"""________________ ________________________ ______________________ ________________________

if saque >= 50:
    notade50 = saque // 50
    novovalor = (saque % 50)
if novovalor >= 40:
    notade20 = novovalor // 20
    novovalor = novovalor % 20
if novovalor >= 10:
    notade10 = novovalor // 10
    novovalor = novovalor % 10


print(notade50, notade20, notade10, novovalor)
"""
