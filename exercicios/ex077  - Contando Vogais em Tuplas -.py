"""_________________ _________________ _________________ _________________ _________________
Crie um Pg que tenha uma tupla com várias palavras (sem acento). Depois disso
, você deve mostrar para cada palavra, quais suas vogais.
_________________ _________________ _________________ _________________ _________________ """

lista = ('Oi', 'tudo', 'bem', 'com', 'voce', 'como', 'esta', 'seu',
         'dia', 'nao', 'esqueça', 'estudar', 'python', 'maravilhoso')

for palavra in lista:
    print(f'\n A vogais da palavra {palavra.upper()} são: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')