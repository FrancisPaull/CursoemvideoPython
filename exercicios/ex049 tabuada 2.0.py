'''Faça uma tabuada utilizando a estrutura de repetição for'''
contagem = 0
tabuada = int(input('Bem vindo ao Tabuada 2.0,'
                    ' Digite um número para saber sua tabuada: '))
for c in range(1,11):
    print('{} * {} = {}'.format(tabuada, c, c * tabuada))