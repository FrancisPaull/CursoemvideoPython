'''
Faça um pg que leia uma frase pelo teclado e mostre:

    --Quantas vezes a letra 'a' aparece.
    --em que posição ela aparece a primeira vez.
    --em que posição ela aparece pela última vez.
'''

frase = str(input('Digite uma frase: ')).upper().strip()
print(frase.count('A'))
print('a letra a aparece a primeira vez na posição {} da string.'.format(frase.find('A')+1))
print('a letra a aparece a última vez na posição {} da sting'.format(frase.rfind('A')+1))