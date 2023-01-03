"""________________ ________________ ________________ ________________ ________________ ________________
Crie um pg que leia nome sexo idade de várias pessoas, guardadando os dados de em um didionário,
e todos dicionários em uma lista. No final mostre:
1- Quantas pessoas cadastradas
2-A média de idade
3- Uma lista com mulherers
3- Uma lista com idade acima da média.
________________ ________________ ________________ ________________ ________________ ________________"""

cadstro = {}
lista = []

total = mediaidade = cont = 0
while True:
    cadstro.clear()
    cadstro['Nome'] = input('Nome: ')
    while True:
        cadstro['Sexo'] = input('Sexo: ').upper()[0]
        if cadstro['Sexo'] in 'MF':
            break
        print('Erro')
    cadstro['Idade'] = int(input('Idade:'))
    total += cadstro['Idade']
    lista.append(cadstro.copy())
    while True:
        resp = str(input('Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
mediaidade = total / len(lista)
print(f'A) Ao todo foram {len(lista)} pessoas cadastradas. ')
print(f'B) a Média de idade é de {mediaidade}')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoas in lista:
    if pessoas['Sexo'] in 'F':
        print(f'{pessoas["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for pessoas in lista:
    if pessoas['Idade'] >= mediaidade:
        print('     ')
        for k, v in pessoas.items():
            print(f'{k} = {v}', end='')




