# faça um programa que leia a largura e altura de uma parede em metros e calcule sua área e a quantidadae de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta 2m².

a = int(input('Digite a altura da parede: '))
l = int(input('Digite a largura da parede: '))
at = a * l
tinta = at // 2
print('O valor total da área a ser pintada é {}, será necessário aproximadanente {} litros de tinta.'.format(at, tinta))

