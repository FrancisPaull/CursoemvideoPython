"""_____________________ _____________________ _____________________ _____________________ _____________________
Melhore o ex anterior, mostrando no final:
1- Soma de todos os valores pares digitados.
2- A soma dos valores da terceira coluna
3- O maior valor da segunda linha
_____________________ _____________________ _____________________ _____________________ _____________________"""

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
somapares = somaterceira = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            somaterceira += matriz[l][c]

print('-=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^7}', end=' ')
    print()
print('-=' * 30)
maiorsegundalinha = max(matriz[1])
print(soma)
print(somaterceira)
print(maiorsegundalinha)