'''Refaça o pg do ex 051 utilizando a estrutura de repetição while'''


primeiro = int(input('10 primeiros termos de uma PA,'
              'Digite um número: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Fim')