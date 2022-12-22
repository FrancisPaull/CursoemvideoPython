'''Crie um pg que leia uma frase qualquer e diga se ela é um ´palindromo desconsiderando os espaços:'''

frase = input('Digite uma frase para descobrir se ela é um Palíndromo: ').upper().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)