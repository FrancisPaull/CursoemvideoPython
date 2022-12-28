""" __________________ __________________ __________________ __________________ __________________
Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol na ordem de
colocação e mostrs:
1- 0s 5 primeiros.
2- Os 4 últimos.
3- Times em ordem alfabética.
4- Em que posição o Time do Flamengo esta.
__________________ __________________ __________________ __________________ __________________ """

lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corithians', 'Flamengo', 'Paranaense', 'Atlético Mineiro',
         'Fortaleza', 'São Paulo', 'América','Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Cutitiba', 'Cuiaá', 'Ceará',
         'Goianiense','Avaí', 'Juventude')

print(lista[0:5])
print(lista[-4:])
print(sorted(lista))
print(lista.index("Flamengo") + 1)