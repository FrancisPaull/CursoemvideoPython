"""_____________ _____________ _____________ _____________ _____________ _____________
Faça um pg que tenha um função chamada área, que receba as dimensões de um terreno retangular e
mostre a área do terreno
_____________ _____________ _____________ _____________ __________________________"""


def area(l, c):
    mquadrado = l * c
    print(f'A área do terreno com {l} de largura por {c} de comprimeto = {mquadrado}m².')


# programa principal
l = int(input('Digite a Largura do Terreno: '))
c = int(input('Digite o comprimento do terreno: '))
area(l,c)