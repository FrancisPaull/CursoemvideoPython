'''Melhore o ex28, o jogador terá que tentar até acertar e no final mostrar quantas tentativas foram realizadas'''

from random import randint
cont = 0
palpite = 100
pc = randint(0,10)
print(pc)
while pc != palpite:
    palpite = int(input('Qual seu palpite: '))
    cont += 1
    if pc > palpite:
        print('Mais..')
    else:
        print('Menos')
print('Parabéns vc acertou após {} tentativas'.format(cont))
