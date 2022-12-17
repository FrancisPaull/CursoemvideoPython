'''
Escreva um pg para aprovar um empréstimo bancário para a compra de uma casa. o pg vai perguntar o valor da casa,
o salário do comprador e em quanos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
import time
print('Bem vindo ao facilitador da casa própria.')
casa = float(input('Qual valor da casa? '))
tempo = int(input('Em quantos anos gostaria de financiar a casa? '))
salario = float(input('Por favor, informe seu salário: '))
print('Aguardando os calculos do sistema...'
      ''
      '')




time.sleep(2)
meses = tempo * 12
prestacao = casa / meses
trintaporcento = ((salario * 30) / 100)
if prestacao < trintaporcento:
    print('Parabéns, seu empréstimo foi APROVADO!')
else:
    print('Infelizmente, no momento, seu empréstimo não foi aprovado.')
