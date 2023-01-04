"""__________________________ __________________________ __________________________ __________________________
Crie uma pg que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o número
para fatorar e o outro chamado show, que será um valor lógico opcional, indicando se irá ou não
mostrar o cálculo na tela.
__________________________ __________________________ __________________________ __________________________"""      # Enunciado


def fatorial(n, show=False):
    """
    Clacula o fatorial de um número
    :param n: Número a ser fatorado
    :param show: Se verdadeiro, vai retornar o cálculo completo
    :return: vai retornar o resultado da fatoração.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='-> ')
    print(f'{f}')
    print()


# Programa principal
fatorial(5,show=True )
help(fatorial)