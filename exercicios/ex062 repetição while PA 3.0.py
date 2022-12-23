'''Melhore o exercício anterior, perguntano ao usuário se ele quer mostrar mais alguns termos,
e quando o 0 for digitado encerre o prograa e mostre quantos termos foram mostrados'''

primeiro = int(input('10 primeiros termos de uma PA,'
              'Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo, end='->'))
        termo += razao
        cont += 1
    mais = int(input('Quantos termo mais ?'))