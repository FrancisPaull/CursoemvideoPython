"""______________ ______________ ______________ ______________ ______________ ______________
Faça um pg que tenha uma função chamada maior(), que receba vários parâmetros, com valores inteiros.
Seu programa tem que analisar todos e dizer qual o maior.
______________ ______________ ______________ ______________ ______________ ______________ """


def linha():
    print('-'*30)


def qualmaior(*num):
    cont = maior = 0
    print(f'\nLendos os valores...')
    for numero in num:
        print(f'{numero}', end=' ')
        print('-', end=' ')
        if cont == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        cont += 1
    print(f'O maior valor digitado foi {maior}.')
    linha()


qualmaior(1, 2, 4, 90, 4)
qualmaior(2,4,9)
qualmaior(1)
qualmaior()
qualmaior(2323, 2)


"""def maior(* num):
    cont = maior = 0
    print(f' Analisando os valores..')
    for valor in num:
        print(f'{valor}', end='')
        if cont == 0:
            maior = valor
        else:
            if: valor > maior:
                maior = valor
        cont +=1
"""


