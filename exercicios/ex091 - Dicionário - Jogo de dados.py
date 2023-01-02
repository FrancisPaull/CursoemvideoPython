"""
Crie um pg onde 4 jogadores joguem um dadoe tenham resultados Aleatórios.
guarde os dados em um dicionário. no final coloque esse dicionários em ordem.

"""

from random import randint
from operator import itemgetter
jogos = {
        'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
ranking = []
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v}')
