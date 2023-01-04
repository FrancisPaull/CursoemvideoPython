"""__________________________ __________________________ __________________________ __________________________
Crie um pg que tenha uma função leiaint(), que vai funcionar de forma semelhante ao input() do python,
Só que fazendo a validação para aceitar apenas um valor númerico. ex "leiaint('Digite um numero')"
__________________________ __________________________ __________________________ __________________________ """     # Enunciado


def leiaint(txt, num=0):
        global n

        while True:
            return input(txt)



n = leiaint('Digite: ')
print(f'Você digitou o número {n} ')