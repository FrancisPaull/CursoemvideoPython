"""_______________ ________________________ ______________________ ____________________
Crie um pg que tenha uma tupla totalmente preenchida com uma contagem por extenso. de zero até vinte.
O Pg deverá ler um número pelo teclado e mostrá-lo por extenso na tela.
_______________ ________________________ ______________________ ____________________"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número: '))

    if num <= 20 and num >= 0:
        print(f'Voce digitou o número {extenso[num]}.', end='')
        mais = str(input(' Quer continuar ?'))
        if mais in 'Nn':
            break
    else:
        continue


print('Obrigado, Volte sempre !')