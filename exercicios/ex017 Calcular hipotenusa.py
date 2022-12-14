#Faça um pg que lei o comprimento do cateto oposto e do cateto adjacente de um retângulo triangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catetoa = float(input('Digite o valor do cateto oposto:'))
catetob = float(input('Digite o valor do cateto adjacente:'))
hipotenusa = hypot(catetoa, catetob)
print('o valor da hipotenusa é {}'.format(hipotenusa))