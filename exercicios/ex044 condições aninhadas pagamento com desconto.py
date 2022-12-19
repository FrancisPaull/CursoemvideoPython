'''
elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
- A vista dinheiro/cheque - 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

'''

preco = float(input('Digite o valor do produto:'))
menu = int(input('''Escolha uma das opções: 
                    [0] Para comprar a vista No dinheiro ou cheque.
                    [1] Para compra a vista no cartão.
                    [2] Para compra parcelada no cartão.
                    '''))
if menu == 0:
    print('O valor total da compra é {}'.format(preco - (preco / 100 * 10)))
elif menu == 1:
    print('O valor total da compra é {}'.format(preco - (preco / 100 * 5)))
elif menu == 2:
    parcelas = int(input('Digite a quatidade de parcelas.'))
    valorparcela = preco / parcelas
    if parcelas <= 2:
        print(' O valor total da compra é {}, o valor da cada parcela será {}'.format(preco, valorparcela))
    else:
        novopreco = (preco / 100 * 20) + preco
        valorparcela = novopreco / parcelas
        print('O valor total da compra é {}, o valor de cada parcela será {}'.format(preco + (preco / 100 * 20), valorparcela))
