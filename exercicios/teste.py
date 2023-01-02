estado = dict()
brasil = list()
for c in range(0,3):
    estado['Uf'] = str(input('Estado: '))
    estado['Sigla'] = str(input('Siglas: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{v} -- {k}')