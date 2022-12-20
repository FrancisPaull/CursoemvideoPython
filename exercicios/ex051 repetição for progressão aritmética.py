'''Crie um pg que leia o primeiro termo e a razão de uma PA e no finaç mosre os 10 primeiros termos dessa progressão:'''


primeiro = int(input('10 primeiros termos de uma PA,'
              'Digite um número: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Fim')