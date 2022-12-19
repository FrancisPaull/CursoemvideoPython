'''
Faça um pg que leia o peso e altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela:
-abaixo de 18,5: abaixo do peso
-entre 18,5 e 25: peso ideal
-25 a 30: sobrepeso
-30 a 40: obesidade
acima de 40 obesidade mórbida
'''
#valor do opeso vezes o valor da altura ao quadrado

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso * (altura ** 2)
if imc < 18.5:
    print('Você esta abaixo do peso.')
elif imc < 25:
    print('Seu peso é ideal')
elif imc < 30:
    print('Você esta com sobrepeso.')
elif imc < 40:
    print('Você esta com obeso.')
else:
    print('Você esta com obesidade mórbida.')