"""________________ ________________ ________________ ________________ ________________
Crie um pequeno sistemo modularizado que permita cadastrar pessoas pelo seu nome e idade em
um arquivo de texto simples. O sistema só vai ter duas opções: cadastrar nova pessoa e
litar todas as pessoas cadastradas.
________________ ________________ ________________ ________________ ________________ """
from modulos.ex115.interface import *
from modulos.ex115.arquivo import *
from time import sleep

arq = 'cadastropessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


def pontoFlutuante():
        for c in range(0,4):
            print('.', end=' ')
            sleep(.5)
        print()


while True:
    resposta = (menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoa.', 'Sair do sistema.']))
    if resposta == 1:
        vercadastro(arq)
    elif resposta == 2:
        nome = input('Nome: ')
        while True:
            try:
                idade = int(input('Idade: '))
            except ValueError:
                print(f'{cor["vermelho"]}{"Digite um valor válido"}{cor["limpa"]}')
            else:
                break
        idade = str(idade)
        print('Adicionando cadastro!', end='')
        pontoFlutuante()
        adicionarcadastro(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        print(f'{cor["vermelho"]}por favor, digite uma opção válida{cor["limpa"]} ')


print(f'{cor["amarelo"]}{"Volte sempre"}{cor["limpoa"]}')