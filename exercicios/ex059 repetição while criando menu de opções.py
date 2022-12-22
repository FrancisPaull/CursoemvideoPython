'''Crie um pg que leia 2 valores e mostre um menu com os seguintes parâmetros:
[1]Somar
[2]Multiplcar
[3] maior
[4] novos números
[5] Sair do programa

'''
r = 0
menu = 5
print('''Escolha uma das opções: 
                    [1] Para somar .
                    [2] Para multiplicar.
                    [3] Para saber qual o maior valor .
                    [4] Para inserir novos números.
                    [5] Para sair do programa.''')
while menu != 0 or menu == 4:
    print('=-='*15)
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    menu = int(input('Digite qual função gostaria de utilizar: '))
    if menu == 4:
        print('Insira novos números.')
    if menu == 0:
        print('Obrigado por usar nosso programa.')
    elif menu == 1:
        r = n1 + n2
        print('A Soma de {} com {} é igual a {}.'.format(n1, n2, r))
    elif menu == 2:
        r = n1 * n2
        print('O resultado da multiplicação entre {} e {} é igual a {}'.format(n1, n2, r))
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}'. format(n1,n2))
        else:
            print('{} é menor que {}'.format(n2, n1))
    elif menu == 0:
        print('Obrigado por usar nosso programa.')




