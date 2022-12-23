'''Refaça o pg do ex 051 utilizando a estrutura de repetição while'''


primeiro = int(input('10 primeiros termos de uma PA,'
              'Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
termo = primeiro
while cont != 10:
    print('{}'.format(termo), end='->')
    cont += 1
    termo += razao
print('Fim')