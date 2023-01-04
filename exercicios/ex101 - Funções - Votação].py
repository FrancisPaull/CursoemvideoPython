"""___________________ ___________________ ___________________ ___________________ ___________________
Crie um pg que tenha uma  função chamada voto(), que vai receber como parâmetro, o ano de nascimento
de uma passoa. retornando um valor literal, indicando se uma pessoa, negado, opcional ou obrigatório
nas eleições.
___________________ ___________________ ___________________ ___________________ ___________________ """     # Enunciado


def voto(num):
    from datetime import datetime
    idade = datetime.now().year - num
    if idade <= 15:
        return f'Desculpe ainda não está hora de vc votar, faltam {16-idade} anos para vc poder votar'
    elif 15 < idade < 18 or idade > 70:
        return f'Você pode votar, mas não é obrigatório'
    else:
        return f'O seu voto é obrigatório!'


while True:
    ano = int(input('Digite seu ano de nascimento: '))
    print(voto(ano))