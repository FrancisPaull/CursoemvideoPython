"""
Diferente das tuplas, as listas podem ser alteradas utilizando comandos específicos.

"""

lanche = ['batata', 'refrigerante', 'sorvete', 'Petit Gateuo', 'hotdog', 'refri diet'  ]

lanche.append('suco')   # Adiciona o elemento ao final da lista.
print(lanche)
lanche[1] = 'potato'
lanche.insert(0, 'hamburguer')  # ( 0 ) antes da vírgula indica onde ser inserido o elemento, que é indicado após a vírgula.'''

# Para remover objetos de uma lista pode-se usar os seguintes comandos:'''

del lanche[2]       # O núnmero [2] indica qual posição quer deletar.'''
lanche.pop(1)   # .pop quando não é utilizado índice(parâmetro) exclui o último eleemnto da lista'''
lanche.remove('suco')   # Utilizado quando o cliente quer excluir o elemento através do nome.'''

'''# Deletar utilizando condição'''

if 'suco' in lanche:
    lanche.remove('suco')

'''# Através da função "list" vc tbm pode declarar outras listas: "valores = lista(range(0,11))"
     Os valores podem ser organizados utilizando a função "valor.sort()". Para que a organização 
     comece de trás pra frente utiliza-se um parâmetro: "valor.sort(reverse=True)"
________________________________________________________
        AULA PRÁTICA
________________________________________________________        
'''
num = [2,5,7,8,9]
num[2] = 1   # Substituir o elemento na posição [2] : "num[2] = 'novoelemento'"
num.append(6)   # adicionar elemento entre parenteses no final da lista
num.sort(reverse=True) # Colocar em ordem decrescente. para ordem crescente não utiliza parâmetro: 'num.sort()'
num.insert(2, 3)    # Para inserir elementos. o primeiro parâmetro indica qual posição (2), o segundo qual o elemento (3)
num.pop()   # para remover o ultimo elemento da lista, caso queira excluir elemento em outra posição utiliza o parâmentro
print(num)
print(f'essa lista tem {len(num)} itens.')    # saber quantos elementos tem na lista.
print(num.index(8))

valores = list()
valores.append(2)
valores.append(5)
valores.append(7)
for c, v in enumerate(valores):    # E numerate expõe tanto a posição quanto o elemento (a chave e o valor)
    print(f'Na posição {c} está o número {v}.')
print('Fim da lista.')

for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))

"""
OS ELEMENTOS PODEM SER COPIADOS UTILZANDO: "copialista = lista[:]", dessa maneira os elementos serão copiados para 
o novo valor. Caso estivesse sem parâmentro, a lista seria interligada uma com a outra, fazendo com que, quando 
alterado um elemento dentro de uma das listas as duas serão modificadas.  
"""