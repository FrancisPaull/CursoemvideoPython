"""____________________ ____________________ ____________________ ____________________ ____________________
Crie um pg que leia quatro números e guarde-os em uma tupla e mostre no final:
1- Quantas vezes apareceu o 9
2- Em que posição apareceu o valor 3
3 - Quais foram os números pares.
____________________ ____________________ ____________________ ____________________ ____________________"""
cont3 = cont9 = 0

lista = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
for n in lista:
    if n == 9:
        cont9 +=1
print(f'O número 9 aparece {cont9} vezes.')
print(f'O número 9 aparece {lista.count(9)} vezes.') #  QUANTAS VEZES O ELEMENTO APARECE NA TUPLA
if 3 in lista:
    print(f'o Número 3 aparece na {lista.index(3) +1}ª posição.')

print(f'Os números pares digitados são: ', end='')
for l in lista:
    if l % 2 == 0:
        print(l, end='-')
print('fim')