'''
Crie um pg que leia o nome de uma cidade e diga se ela começa com 'Santo' ou não.
'''

cidade = str(input('Digite o nome da cidade: ')).upper().strip()
print(cidade[:5] == 'SANTO')
