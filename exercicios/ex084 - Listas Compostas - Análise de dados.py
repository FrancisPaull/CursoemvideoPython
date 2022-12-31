"""________________ ________________ ________________ ________________ ________________
Faça um pg que leia o nome e o peso de várias pessoas colocado-as numa lista e mostre:
1-Quantas pessoas foram cadastradas
2- Uma listagem com as pessoas mais pesadas             70 ou menos - leves
3- uma listagem com as pessoas mais leves               100 ou mais - pesados
________________ ________________ ________________ ________________ ________________"""

principal = list()
temporario = list()
maior = menor  = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(temporario) == 0:
        maior = menor = temporario[1]
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()

    continuar = str(input('Continuar [S/N]? '))
    if continuar in 'Nn':
        break















"""______________________________ ______________________________ ______________________________ 
lista = []
pesados = []
leves = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    if peso <= 70:
        leves.append(nome)
        leves.append(peso)
    elif peso >= 100:
        pesados.append(nome)
        pesados.append(peso)

    resp = str(input('Continuar [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'o maior peso foi')
print(pesados)
"""