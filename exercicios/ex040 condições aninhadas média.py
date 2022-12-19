'''
Crie um Pg que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final, de acordo com a
média atingida.
-Média abaixo de 5.0 reprovado
-média entr 5,0 e 6,9 recuperação
-média maior que 6,9 aprovado
'''
n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Que pena você esta reprovado!')
elif media < 7 and media > 4.9:
    print('Você esta de recuperação.')
else:
    print('Parabéns, você esta APROVADO!')