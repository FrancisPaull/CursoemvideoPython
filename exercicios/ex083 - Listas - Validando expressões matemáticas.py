"""_________________ _________________ _________________ _________________ _________________
Crie um pg que o usuário digite uma expressão qualquer que use parenteses, Seu aplicativo deverá
analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.
_________________ _________________ _________________ _________________ _________________ """

lista = list(str(input('Digite um expressão: ')))
x = 0
for c in lista:
    if c == '(':
        x += 1
    if c == ')':
        x -= 1
    if x < 0:
        break
if x == 0:
    print('A expressão está correta!!')
else:
    print('Sua expressão está errada!')