"""________________ _________________ _________________ _________________ _________________
Crie um pg onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. caso o número já
exista na lista ele não será adicionado novamente. No final, serão exibidos todos os valores únicos
digitados em ordem crescente.
_________________ _________________ _________________ _________________ _________________"""

lista = list()

while True:
    n = int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)
        print('Número Adicionado')
    else:
        print('Número não adicionado.')
    mais = str(input('Gostaria de adicionar mais números? [S/N]'))
    if mais in 'Nn':
        break
print(sorted(lista))

