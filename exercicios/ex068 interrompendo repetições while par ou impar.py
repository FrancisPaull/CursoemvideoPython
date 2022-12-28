""" __________________________________________________________________________________
Faça um pg que jogue par ou impar com o pc, o jogo ser´interrompido se o jogador perder
mostrando a total de vitórias consecutivas ele conquistou
__________________________________________________________ """

from random import randint
choice = ' '
vitoria = 0
while True:
    numero = int(input('Digite um número: '))
    choice = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    while choice not in 'PI':
        choice = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    computador = randint(1, 10)
    resultado = computador + numero
    if resultado % 2 == 0 and choice[0] in 'P':
        print('Você ganhou!')
        vitoria += 1
    elif resultado % 2 == 1 and choice[0] in 'I':
        print('Você ganhou')
        vitoria += 1
    else:
        print(f'você perdeu e teve {vitoria} vitórias consecutivas !')
        break








"""
________________________________________________________________________________________
pc = randint(1, 10)
resultado = ''
jogador = ''
opcao = 'a'
ganhador = ''
cont = 1
while True:
    if opcao == resultado:
        print('Você Ganhou, vamos jogar outra vez? ')
        cont = +1
        pc = randint(1, 10)
    while True:
        opcao = str(input('Par ou Ímpar? [P/I]')).strip().upper()
        if opcao == 'P' or opcao == 'I':
            break

    jogador = int(input('Qual número?   '))

    resultado = pc + jogador
    if resultado % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if opcao != resultado:
        print('Você perdeu!')
        print(f'Você ganhou {cont} vezes consecutivas!')
        break
        
        """
