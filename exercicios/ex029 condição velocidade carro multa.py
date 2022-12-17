'''
Faça um pg que leia a velocidade de um carro e: se ele estiver acima de 80km/h mostre uma mensagem que ele foi multado
A multa vai custar R$7 por cada km acima do limite.
'''

velocidade = int(input('Digite qual velocidade do seu carro: '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print('Cuidado" Você esta {}km/h acima do limite, Você foi multado em R${}, seja mais cuidadoso.'.format(excesso, multa))
else:
    print('Boa viagem!')
