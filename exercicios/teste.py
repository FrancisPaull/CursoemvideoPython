cadstro = {}
lista = []
while True:
    cadstro['nome'] = input('Nome')
    while True:
        cadstro['sexo'] = input('sexo').upper()[0]
        if cadstro['sexo'] in 'MF':
            break
        print('Erro')
    cadstro['idade'] = int(input('Idade:'))
    lista.append(cadstro.copy())
    while True:
        resp = str(input('Continuar ? '))
        if resp in 'SN':
            break
    if resp == 'N':
        break