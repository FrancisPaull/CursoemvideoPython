'''Crie ym pg que leia vários números inteiros pelo teclado e no final mostre a média entre todos, qual foi o menor
e qual foi o maior número digitado, perguntando ao usuário se ele quer ou não adicionar mais valores.'''
n = int(input('Digite um número: '))
menor = n
maior = n
soma = n
cont = 1
adicionar = str(input('Gostaria de adicionar mais [S/N]? ')).upper().strip()
while adicionar not in 'N':
    n = int(input('Digite um número'))
    adicionar = str(input('Gostaria de adicionar mais [S/N]? ')).upper().strip()
    if n < maior and n < menor:
        menor = n
    elif n > menor and n > maior:
        maior = n
    soma += n
    cont += 1
    media = soma / cont
print('Você digitou {} números, a média detodos os valores digitados é {}, {} foi o menor número digitado e {} foi o maior.'.format(cont, media, menor, maior))