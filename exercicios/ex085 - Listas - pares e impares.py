"""_________________ _________________ _________________ _________________ _________________
Crie um pg onde o usuário pode digitar 7 valores e cadastre-os em uma única lista. que mantenha separada os valores
pares e ímpares. mostre no final os valores pares e ímapres em ordem crescente.
_________________ _________________ _________________ _________________ _________________"""

lista = [[], []]
for c in range(1, 8):
    n = (int(input(f'Digite o {c}º valor: ')))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()

print(f'Os números pares são: {lista[0]}')
print(f'Os números ímpares são {lista[1]}')
