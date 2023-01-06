"""________________ ________________ ________________  ________________ ________________
reescreva a função leiaint(), incluindo agora a possibilidade da digitação errada, retornando como
inválido, crie tbm uma função com nome leiafolat() com a mesma funcionalidade.
________________ ________________ ________________ ________________ ________________"""  # Enunciado


def leiaint(txt):
    ok = False
    valor = 0
    while True:
        n = input(txt)
        if n.isnumeric():
            ok = True
            return n
        else:
            print('Invalálido.')
        if ok:
            break


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print(f'por favor digite um inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada cancelada pelo usuário')
            continue
        else:
            return n


# Programa Principal
num = leiafloat('Digite um valor: ')
print(f'O valor digitado foi {num}')
