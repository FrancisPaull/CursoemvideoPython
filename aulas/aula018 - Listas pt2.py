"""______________________ ______________________ ______________________ ______________________

______________________ ______________________ ______________________ ______________________"""

teste = []
teste.append('Francis')
teste.append((34))
galera = list()
galera.append(teste[:])
teste[0] = 'Paul'
teste[1] = 35

galerateste = [['Pedro', 22], ['Paulo', 43], ['Ana', 22], ['Maria', 35]]
print(galerateste[2][1])    # Utiliza 2 parâmetros para acessar lista dentro de lista.
for pessoas in galerateste:
    print(pessoas[1]) #Utiliza o parâmentro para definir qual elemento acessar na lista
for pessoas in galerateste:
    print(f' {pessoas[0]}, tem {pessoas[1]} anos de idade')

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Utiliza o parâmentro para fazer uma cópia da lista dentro da outra, caso não, elas seriam interligadas.
    dado.clear()
menores = maiores = 0
for pessoas in galera:
    if pessoas[1] < 18:
        print(f'{pessoas[0]} é menor de idade')
        menores += 1
    else:
        print(f'{pessoas[0]} é maior de idade.')
        maiores += 1
print(f'Tota de {maiores} pessoas maiores de idade e {menores} menores.')













#nada