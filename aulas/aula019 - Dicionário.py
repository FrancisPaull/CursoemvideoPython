

#dados = dict()
#dados = {}  # Para declarar um dicionário.
lista = list()
dados = {'nome': 'Paul', 'idade': 34}
lista.append(dados)     #dicionários podem ser adicionados em listas

print(dados['idade'])
print(dados['nome'])
dados['sexo'] = 'M'
print(dados)
del dados['sexo']
print(dados)
print()
print(dados.values())   #Vai mostrar os valores do dicionário
print(dados.keys())    #Para printar as chaves
print(dados.items()) #Vai printar os itens, em conjunto ('nome': 'Paul')
print()
for key, value in dados.items():
    print(f' {key} é {value}')

"""
Os dicionários podem ser utilizados dentro de uma lista, lembrando que os índices de uma lista são identificados por 
números. o acesso aos itens de um dicionário dentro de uma lista seriam da seguinte maneira: print(lista[0]['nome'])

"""
print('-='*25,'ex1')

pessoas = {'nome': 'Francis', 'sexo': 'M', 'idade': 34}
for key in pessoas.keys():
    print(key)
print('-='*25,'ex2')
for key in pessoas.values():
    print(key)
print('-='*25,'ex3')
for key, values in pessoas.items():
    print(f'{key} é {values}')
print()
print('-='*25)
print(str('-= Criando dicionário dentro de uma lista'))
print('-='*25)
print('Ex04')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print()
print('=-=--Ex05')
print()

estados = {}
brasil1 = []
for c in range(0, 3):
    estados['uf'] = str(input('Estado: '))
    estados['Sigla'] = str(input('Sigla do estado: '))
    brasil1.append(estados.copy())
print()
print()
for e in brasil1:
    print(e)
    for key, value in estados.items():
        print(f'A chave é {key} e o valor é {value}.')
print(estados.items())


print()
print()
print()
print()
print()












#test