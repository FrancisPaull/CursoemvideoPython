"""_________________ _________________ _________________ _________________ _________________
Crie um pg que leia vários números e coloque em uma lista e depois mostre:
1- Quantos números foram digitados
2-A lista de valores, ordenada de forma decrescente
3- Se o número 5 foi digitado e se está ou não na lista.
_________________ _________________ _________________ _________________ _________________ """
lista = []
while True:
    lista.append(int(input('Digite um número')))
    mais = str(input('Gostaria de adicionar mais? [S/N]? '))
    if mais in 'Nn':
        break
print(f'Você digitou {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista:')
else:
    print(f'O valor 5 Não faz parte da lista:')