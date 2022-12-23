'''Faça um pg que faça a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário
o programa será interrompido quando o número solicitado for negativo
____________________________________________________________________________________________________'''

n = cont =0

while True:
    print('=-=' * 30)
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:
        break
    for tabuada in range(1,11):

        print(f'{n} * {tabuada} = {n*tabuada}')


