"""_________________ _________________ _________________ _________________ _________________
Crie um pg que vai ler vários números e colocar em uma lista, depois disso, crie duas listas extras, que vão
conter apenas os valores pares e os valores ímpares respectivamente. Ao final mostre o conteúdo das três listas.
_________________ _________________ _________________ _________________ _________________ """

lista = list()
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    resp = str(input('Adicionar mais [S/N]? '))
    if resp in 'Nn':
        break
print(f'Valores adicionados: {lista}.')
print(f' Somente os valores pares: {listapar}.')
print(f'Somente os valores ímpares: {listaimpar}.')