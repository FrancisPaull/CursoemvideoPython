"""__________________________ __________________________ __________________________ __________________________
Faça um pg que tenha uma função chamada ficha(), que receba dois parâmetros opicionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
__________________________ __________________________ __________________________ __________________________"""      # Enunciado


def ficha(jogador ='Desconhecido', g=0):
    return f'O jogador {jogador} fez {g} gol(s) na partida.'


nome = input('Nome do Jogador: ')
gols = input('Quantos gols? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))