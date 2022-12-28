"""_________________________ _________________________ _________________________ _________________________
Crie um Pg que tenha uma tupla única com nomes de produtos e seus respectivos preços. na sequência.
no final, mostre uma listagem de preços organizados em forma de tabela.
_________________________ _________________________ _________________________ _________________________"""

lista = ( 'Lápis',1.80,
          'Borracha', 2.00,
          'Caneta', 5.52,
          'Caderno', 17.80,
          'Fichário', 38.00,
          'Livro', 125.00
          )
print('-=' * 30)
print(f'{"Listagem de Preços":^50}')
print('-='*30)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')# O ( . ) Vai preencher o parágrafo com sinal ----( < ) indica alinhamento a esquerda
    else:
        print(f'R$ {lista[posicao]:>.2f}')


