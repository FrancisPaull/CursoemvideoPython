'''Faça um programa que mostre na tela uma contagem regressiva com pau sa de 1min.'''
import time
for c in range(10, 0, -1):
    time.sleep(0.5)
    print(c)
print('Fim')