'''
Escreva um pg que leia um numero inteiro qualquer e peça o usuário escolher qual será a base de conversão:
1 -  binério
2 -  octal
3 - hexadecimal
'''
n = int(input('Digite um número: '))
opcao = int(input('''Conversão de números inteiros:
                    [1] Para converter em número binário
                    [2] Para converter em número Octal
                    [3] Para converter em número hexadecimal
'''))
if opcao == 1:
    n = bin(n)
    print('O valor convertido em binário é: {}'.format(n))
elif opcao == 2:
    n = oct(n)
    print('O valor convertido em octal é {}.'.format(n))
elif opcao == 3:
    n = hex(n)
    print('O valor conertido em Hecadecimal é {}'.format(n))
