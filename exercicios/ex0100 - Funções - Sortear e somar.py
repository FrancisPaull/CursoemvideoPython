"""_____________________ _____________________ _____________________ _____________________ _____________________
Faça um pg que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
a primeira função vai sortear 5 números e vai colocálos dentro de uma lista o segundo
vai fazer a soma de todos números pares sorteados pela função.
_____________________ _____________________ _____________________ _____________________ _____________________"""  # Enunciado
from random import randint


def sorteia(lista):
    for c in range(1,6):
        lista.append(randint(1,20))
    print(lista)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)


num = list()
sorteia(num)
somapar(num)