'''Escreva um pg que leia um número inteiro e mostre na tela os n primeiros elementos de uma sequencia de fibonacci'''


termo = int(input('Quantos termos da sequencia de fibo gostaria de mostrar? '))
primeiro = 0
segundo = 1
for c in range(primeiro,termo, ):
    print('{}'.format(primeiro), end='-> ')
    primeiro += segundo
