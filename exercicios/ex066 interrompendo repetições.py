'''Crie um pg que leia vários números. oprograma só vai parar quano for digitado o numero 999.
 no final mostre quantos números foram digitados e qual a soma entre eles.
 ____________________________________________________________________________________________'''

cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números, e {soma} é o resultado da soma entre eles.')