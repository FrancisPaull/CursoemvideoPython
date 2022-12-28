'''______________________________________________________________________________________________________
Crie um pg que leia o nome e o preço de vários produtos. o programa deverá perguntar se o usuário vai continuar.
no final mostre:

1-Qual é o total de gasto na compra.
2- Quantos produtos custam mais de 1000.
3 - Qual o nome do produto mais barato.
________________________________________________________________________________________________________'''
soma = maisde1000 = totalprodutos = maisbarato = maiscaro = 0
nomemaisbarato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: '))
    mais = str(input('Quer continuar ? [S/N] ? ')).upper().strip()
    soma += preco
    if preco > 1000:
        maisde1000 += 1
    totalprodutos += 1
    for lista in range(0, totalprodutos):
        if lista == 1:
            maisbarato = preco
        if preco < maisbarato:
            nomemaisbarato = nome
    if mais in 'N':
        break
print(f'Olá, você comprou {totalprodutos} produtos, {maisde1000} produtos custam mais de R$ 1000,00 e {nomemaisbarato} é o nome'
      f'do produto mais barato. O valor total da compra é R${soma}.')