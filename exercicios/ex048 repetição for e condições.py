'''Crie um pg que calcule a soma entre todos os números impares que são múttiplos de três entre 1 e 500'''
soma = 0
for c in range(0,500,3):
    if c % 2 == 1:
        soma += c
print(soma)
print('Fim')