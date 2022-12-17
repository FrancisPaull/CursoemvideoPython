'''
Desenvolva um pg que pergunte a distância de uma viagem em km. Calcule o preço cobrado da passagem.
cobrando 0.5 por hora para viagens de até 200km/h e R$0,45 por viagens mais longas.
'''

distancia = int(input('Para saber o valor da passagem informe qual a distância em KM:'))
if distancia <= 200:
    passagem = distancia * 0.5
    print('O valor da passagem é R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O valor da passagem é R${:.2f}'.format(passagem))