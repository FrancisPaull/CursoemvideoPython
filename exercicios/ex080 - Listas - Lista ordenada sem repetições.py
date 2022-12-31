"""_________________ _________________ _________________ _________________ _________________ _________________
Crie um Pg ondo usuário possa digitar cinco números e cadastre os em uma lista, já na posição correta de inserção.
No final mostre a lista ordenada na tela.
_________________ _________________ _________________ _________________ _________________ _________________"""
lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print(lista)
