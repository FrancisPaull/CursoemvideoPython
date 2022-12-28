'''
Em python existe três tipos de váriaveis composta.
 * Tuplas
 * Listas
 * e Dicionários
 _____________________ _____________________ _____________________ _____________________ _____________________

 lengh = ( len(variável) - lEN MOSTRA O COMPRIMENTO DA VARIÁVEL

 OBS.: AS TUPLAS SÃO IMUTÁVEIS


'''

'''
 _____________________ _____________________ _____________________ _____________________
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[1:3])
 _____________________ _____________________ _____________________ _____________________

'''


'''
 _____________________ _____________________ _____________________ _____________________


lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Fim')

 _____________________ _____________________ _____________________ _____________________

'''

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'

for cont in range(0, len(lanche)):
    print('Eu vou comer {}. '.format(lanche[cont]))

for posicao, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {posicao}')

print(sorted(lanche)) #Organiza a tupla transformando a em uma lista - Colocar en ordem

a = 2, 4, 6, 8
b = 9, 7, 5, 3
c = a + b #Para unir as tuplas, nesse caso a ordem altera o reultado final.
d = b + a
teste = a + b
print(c)
print(d)

del(teste) #Apesar de imutável a tupla pode ser deletada.
print(teste)

print(sorted(d)) #Colocar em ordem

print(d.count(3)) #Para mostrar quantas vezes o elemento dentro do parenteses aparece na tupla.

print(d.index(5, 1)) # o pg vai mostrar qual a posição do elemento. o número 1 neste caso está indicando em qual posição
# o programa vai começar a procurar o elemento
