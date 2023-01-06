frase = 'Ler ao contrário'
lista = [frase]
print(frase)
inicio = len(frase) - 1
while inicio != -1:
    for letra in lista:
        print(letra[inicio],end='')
        inicio -= 1

