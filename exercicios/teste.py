lista = []
for n in range(0,5):
    n = int(input('Diga um valor: '))
    lista += [n]

print(lista)
print(f'O maior valor da lista é {max(lista)} e está na posição {lista.index(max(lista))}')
print(f'O menor valor da lista é {min(lista)} e está na posição {lista.index(min(lista))}')