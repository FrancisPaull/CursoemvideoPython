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
        a = open(nome,'wt+')
        a = a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'O arquivo {nome}, criado com sucesso!')


def adicionarcadastro(arq,nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'a', encoding='UTF-8')
    except FileNotFoundError:
        print('Erro ao abrir o arquivo:')
    try:
        arquivo.write(f'{nome};{idade}\n')
    except:
        print('Erro ao adicionar cadastro.')
    else:
        print(f'{cor["verde"]}Novo registro adicionado.{cor["limpa"]}')
        arquivo.close



def vercadastro(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
       for linhaa in a:
            dado = linhaa.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

