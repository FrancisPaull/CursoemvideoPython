'''
Crie um pg que faça o computador gerar um número inteiro entre 0,5e peça para o usuário tentar descobrir qual o numero
escolhido    pelo PC, informando se o usuário venceu ou perdeu.
'''
from time import sleep
import random
aleatorio = random.randint(0,5)
numero = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if numero == aleatorio:
    print('Parabéns, você acertou!')
else:
    print('Erro bixa, tenta de novo!')
