"""
Faça um pg que leia o nome e a média de um aluno, guardando tbm a situação em um dicionário.
mostre o conteúdo da estrutura na tela

"""

lista = {}
classe = []

lista['Nome'] = (input('Qual nome do aluno'))
lista['Média'] = (float(input('Qual a média do aluno: ')))
if lista['Média'] >= 7:
    lista['Resultado'] = 'Aprovado'
else:
    lista['Resultado'] = 'Reprovado'
classe.append(lista.copy())

for i in classe:
    for k, v in i.items():
        print(f'{k} é igual a {v}')