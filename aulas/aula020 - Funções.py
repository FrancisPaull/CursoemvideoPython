""""
 Interactive Help - Organização de arquivos
 Docstrings - documentação do pos programas
 Argumentos opcionais - funções com argumentos opcionais
 Escopo de variáveis - Em que momento uma variável nasce e em que momento ela morre, em que momentos e
 posições que sua variável esta visível.
 funções que retornam resultados.
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

                            --------Ajuda interativa--------
                                    Interactive Help

help(print) - no console
print(print.__doc__)


                          -----------Docstrings--------------

Documentação das funções - logo abaixo do definir função, utilizar aspas duplas três vezes, para
criar um documento da função, explicando o conteúdo da própria.
help(função)

                        -----------Escopo de variáveis----------

Variavel global - Escopo global - Quando declarada no propgrama principal, funciona em tod0 arquivo.
variável local - Escopo local -  Quando a variável é declarada apenas dentro de uma função, funcionará apenas
naquela função.



"""    # Explicação


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(num=1):
    if num % 2 == 0:
        return True


n = int(input('Digite um número'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

while True:
    nu = int(input('Digite um número para saber se é par ou ímpar.'))
    if par(nu):
        print(f'{nu} é par.')
    else:
        print(f'{nu} é impar.')