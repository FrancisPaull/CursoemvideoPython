"""__________________ __________________ __________________ __________________ __________________
Faça um Pg que gere números aleatórios para o sorteio da mega sena.
__________________ __________________ __________________ __________________ __________________"""
from random import randint
from time import sleep
lista = [0,0,0,0,0,0]
boasorte = 'Boa Sorte!!!'
letra = 0
print()
print('-=*'*30)
print(f'               Bem vindo ao gerador de apostas da Mega Sena!')
print('-=*'*30)
print()
palpites = int(input('Quantos jogos você gostaria de mostrar? '))
print()
for colunas in range(0, palpites):
    for n in range(0,6):
        lista[n] = randint(1,60)
    sleep(0.5)
    print(f'{lista}')
    print()
sleep(0.5)
print('*-'*10, end='')
for letra in range(0, len(boasorte)):
    print(boasorte[letra], end='')
    sleep(0.3)
print()

