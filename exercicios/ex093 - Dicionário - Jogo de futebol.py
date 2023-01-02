"""_______________ _______________ _______________ _______________ _______________ _______________
Crie um pg que gerencie o aproveitamento de um jogador de futebol. o pg vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida.
no final, tudo isso será gardado em um dicionário, incluindo o total de gols feitos surante o campeonato.
_______________ _______________ _______________ _______________ _______________ _______________"""

dados = dict()
gols = []

dados['Nome'] = input('Qual o nome do jogador? ')
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
for c in range(1,partidas +1):
    gol = gols.append(int(input(f'Quantos gols na {c}ª partida?  ')))
dados['gols'] = gols[:]
dados['total de gols'] = sum(gols)
print()
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {dados["Nome"]}, jogou {partidas}.')
for k, v in enumerate(gols):
    print(f'=> Na partida {k+1}, {dados["Nome"]}, fez {v} gols.')
print(f'Total de {dados["total de gols"]} gols.')