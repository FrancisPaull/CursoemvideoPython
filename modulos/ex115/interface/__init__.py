cor = {
            'limpa': '\33[m',
            'azul': '\33[34m',
            'amarelo': '\33[33m',
            'vermelho': '\33[31m',
            'fundoazul': '\33[30;46m',
            'verde': '\33[32m'
    }


def linha():
    print('-' * 40)


def cabeçalho(txt):
    linha()
    print(f'{cor["fundoazul"]}{txt.center(41)}{cor["limpa"]}')
    linha()


def menu(lista):
    cabeçalho('Menu Principal'.upper())
    c = 1
    for item in lista:
        print(f'{cor["amarelo"]}{c}{cor["limpa"]} - {cor["azul"]}{item}{cor["limpa"]} ')
        c += 1
    linha()
    opc = (leiaint(f'{cor["amarelo"]}Qual sua opção?{cor["limpa"]} '))
    linha()
    return opc


def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
            break
        except (ValueError,TypeError):
            print(f'{cor["vermelho"]}Opção inválida{cor["limpa"]}')
            linha()
            continue
    return n






'''def cadastro():
    with open('pessoas', 'a') as arquivo:
        arquivo.write(input(f"{'Nome: '}"))
        while True:
            try:
                idade = leiaint('Idade')
                break
            except:
                print('valor inválido')
                continue
        arquivo.write(f'{idade}')


def vercadastro():
    with open('pessoas', 'r') as arquivo:
        print(arquivo.read())
'''