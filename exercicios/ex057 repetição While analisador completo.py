'''Desenvolva um pg que leia o nome, idade e sexo [m/f] de quatro pessoase no final mostre:
A média de idade do grupo
Quantas mulheres tem menos de 20 anos
qual é o nome do homem mais velho
'''

from datetime import date
ano = date.today().year
cont = 0
somaidade = 0
media = 0
mulheresmenosde20 = 0
homemmaisvelho = 0
idademaisvelho = 0
while cont < 4:
    cont += 1
    nome = input('Digite o nome da {}ª pessoa: '.format(cont))
    sexo = input('Qual o sexo da {}ª pessoa: [M/F]] '.format(cont)).upper().split()
    idade = int(input('Qual idade da {}ª pessoa?'.format(cont)))
    somaidade += idade
    media = somaidade / cont
    if sexo == 'F' and idade < 20:
        mulheresmenosde20 += 1
    else:
        if idade > idademaisvelho:
           homemmaisvelho = nome
           idademaisvelho = idade

print('A média de idade do grupo é de {}, um total de {} mulheres tem menos de 20 anoe e o nome do homem mais velho é {}'
      .format(media, mulheresmenosde20, homemmaisvelho))