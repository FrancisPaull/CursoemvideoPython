'''_________________ _________________ _________________ _________________ _________________
Faça um pg que leia 5 valores númericos e guardeos em uma lista. no final mostre qual
foi o maior e o menor número digitado e suas respectivas posições na lista.
_________________ _________________ _________________ _________________ _________________ '''

lista = list()
for c in range(1, 5):
    lista.append(int(input('Digite um número: ')))
menor = min(lista)
maior = max(lista)
print(f'{lista.index(max(lista))}')
print(f'{lista.index(min(lista))}')
for posicao, valor in enumerate(lista):
    if valor == maior:
        print(f'O maior valor digitado foi {maior} na posição {posicao +1}.')
    if valor == menor:
        print(f'O menor valor digitado foi {menor} na posição {posicao +1}.')







