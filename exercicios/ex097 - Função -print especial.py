"""_____________ _____________ _____________ _____________ _____________ _____________
Faça um pg que tenha um função chamada escreva(), que receba um texto qualquer
como parâmentro e mostre uma mensagem com tamanho adaptável.
_____________ _____________ _____________ _____________ _____________ _____________ """


def escreva(txt):
    frase = str(txt)
    linha = ('*' * len(frase))
    print(linha)
    print(f'{txt:^}')
    print(linha)
    print()


escreva('Olá tudo bem !')
escreva('Testando a função com mais caracteres.')
