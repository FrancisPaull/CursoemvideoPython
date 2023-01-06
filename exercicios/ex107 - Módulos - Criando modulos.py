"""________________ ________________ ________________ ________________ ________________ ________________
Crie um módulo chamado moeda.py que tenha todas as funções incorporada, aumentar(%), diminuir(%), dobro
e metade. Faça tbm um pg que import esse módulo e use essas funções.
________________ ________________ ________________ ________________ ________________ ________________ """       # Enunciado
from modulos import moedas

n = int(input('Digite um valor: '))
print(f'{moedas.aumentar(n, 13, form=True)}')
print(f'{moedas.diminuir(n, 20, form=True)}')
print(f'{moedas.dobro(n)}')
print(f'{moedas.metade(n)}')
moedas.leiadinheiro()