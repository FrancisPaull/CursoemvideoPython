# --Existem funcionalidades dentro dos modos, por exemplo:
# -na biblioteca 'math' existem alguns tipos como:
# ceil (arredonda o número para um maior)
# floor ( arredonda o número para um menor)
# trunc (elimina os números depois da vírgula)
# pow ( potência)
# sqtr (calcular raiz quadrada) (square root)
# factorial (fatorar um número)
# --Pode-se importar toda a bilbioteca ou somente as funções que serão utilizadas no programa separadas por vírgula: **from math import pow** (para usar a funcionalidade de potência.


import math
num = int(input('Digite um número: '))
raiz = math.sqrt((num))
print('A raiz quadrada de {} é igual a {}.'.format(num, math.ceil(raiz)))