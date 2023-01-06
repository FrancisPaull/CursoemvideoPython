

def aumentar(n=0, por=0, form=False):
    n += (n/100) * por
    if form:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n


def diminuir(n=0, por=0,form=False):
    n -= (n / 100) * por
    if form:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n


def dobro(n=0,form=False):
    n = n * 2
    if form:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n



def metade(n=0,form=False):
    n = n / 2
    if form:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n


def leiadinheiro(n=0,form=False):
    while True:
        n = input(f'Digite o preço: ')
        if n.isnumeric():
            break
        else:
            print('\033[031mErro\033[m')
    return f'R${n:.2f}'
