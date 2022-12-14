#Faça um pg queleia um nângulo qualquer e mostre o valor de seno, cosseno e tangete.

import math
n = int(input('Digite o valor do ângulo para saber seu seno, cosseno e tangente:'))
seno = math.sin(n)
cosseno = math.cos(n)
tangente = math.tan(n)
print('O valor do seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(seno, cosseno, tangente))