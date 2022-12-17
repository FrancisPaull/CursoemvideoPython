'''
escreva um pg que leia o salário de um funcionário e calcule o valor de seu aumento baseado em: Para salários maiores
que 1250 o acréssimo é de 10%, para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o valor do seu salário para saber o novo valor com aumento: '))
if salario <= 1250.00:
    aumento =  ((salario/100)*15)
else:
    aumento = ((salario/100)*10)
novo = salario + aumento
print('Você receberá um acrécimo de R${:.2f}, seu novo salário será de {:.2f}'.format(aumento, novo))