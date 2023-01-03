"""_____________ _____________ _____________ _____________ _____________ _____________
Faça um pg que tenha uma função chamda contador(), que receba três parâmetros. início, fim e passo.
Seu pg tem que realizar 3 contagens através da função:
1- de 1 a 10, de 1 em 1
2- de 10 a 0, de 2 em 2
3- uma contagem personalizada
_____________ _____________ _____________ _____________ _____________ _____________ """
from time import sleep


def linha():
    print('*'*30)


def contagem(inicio, fim, passo):

    cont = inicio
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if cont < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
    while inicio >= fim:
        print(f'{inicio}', end=' ')
        inicio -= passo
    print('-> fim')


linha()
contagem(1,10,1)
linha()
contagem(10,1,-1)















'''def contagem(incio, fim, passo):
    for c in range(incio,fim,passo):
        print(c, end=' ->')
        sleep(0.1)
    print('fim')


contagem(1,11, 1)
linha()
contagem(10,-1,-2)
linha()
print('Personalize sua contagem:')
contagem(int(input('Digite o ínicio: '), int(input('Fim: '), int(input('Passo: ')))))'''