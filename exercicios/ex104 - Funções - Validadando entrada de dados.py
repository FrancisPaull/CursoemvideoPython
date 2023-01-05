"""__________________________ __________________________ __________________________ __________________________
Crie um pg que tenha uma função leiaint(), que vai funcionar de forma semelhante ao input() do python,
Só que fazendo a validação para aceitar apenas um valor númerico. ex "leiaint('Digite um numero')"
__________________________ __________________________ __________________________ __________________________ """     # Enunciado


def leiaint(txt, num=0):
    ok = False
    valor = int()
    while True:
        n = input(txt)
        if n.isnumeric():
            ok = True
            valor = n
        else:
            print('\033[0;31mErro!!!\033[mCaracteres inválidos, por favor digite \033[0;33m NÚMEROS INTEIROS.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n} ')