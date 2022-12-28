"""__________________________________________________________________________________________________________
Crie um pg que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada. O programa deverá perguntar se quer
continuar ou não e mostre no final:
1- Quantas pessoas tem mais de 18 anos.
2- Quantos Homens foram cadastrados.
3- Quantas mulheres tem menos de 20 anos.
_____________________________________________________________________________________________________________"""

homens = mulheresmenosde20 = maisde18 = total = 0
sexo = continuar = ''
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).upper().strip()
    continuar = str(input('Gostaria de mostrar mais? ')).upper().strip()
    total += 1
    if idade > 18:
        maisde18 += 1
    if sexo[0] in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheresmenosde20 += 1
    if continuar[0] in 'N':
        break
print(f'Você cadastrou {total} pessoas no total, {homens} homens foram cadastrados e {mulheresmenosde20} mulheres tem menos de 20 anos e {maisde18} pessoas tem mais 18 anos.')