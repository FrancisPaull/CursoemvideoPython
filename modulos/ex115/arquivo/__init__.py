from modulos.ex115.interface import  *


def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt')
        a = a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'O arquivo {nome}, criado com sucesso!')


def adicionarcadastro(arq,nome, idade):
    try:
        a = open(arq, 'a', encoding='UTF-8')
        a.write(nome)
        a.write(idade)
        a = a.close()

    except ValueError:
        print('Valor inválido')


def vercadastro(nome):
    with open(nome, 'r') as arquivo:
        print(arquivo.read())