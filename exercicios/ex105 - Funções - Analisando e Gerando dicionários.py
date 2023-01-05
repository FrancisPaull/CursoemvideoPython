"""_____________________ _____________________ _____________________ _____________________
Faça um pg que tenha uma função notas(), que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
1) Quantidade de notas
2) A maior nota
3) A menor nota
4) A situação opcional
5) docstrings
_____________________ _____________________ _____________________ _____________________ """     # Enunciado


def notas(*num, sit=False):
        """
        Gerador de dicionários.
        :param num: Coloque a quantidade de notas que desejar para saber o resumo.
        :param sit: saida True para saber qual a situação do aluno.
        :return: Irá imprimir os valores do resumo armazenados em um dicionário
        """
        resumo = {}
        resumo['Total'] = len(num)
        resumo['Maior'] = max(num)
        resumo['Menor'] = min(num)
        resumo['Média'] = sum(num) / len(num)
        if sit:
                if resumo['Média'] < 5:
                        resumo['situação'] = 'Ruim'
                elif resumo['Média'] < 7:
                        resumo['situação'] = 'Dentro da Média'
                elif resumo['Média'] < 9:
                        resumo['situação'] = 'Boa'
                else:
                        resumo['situação'] = 'Excelente'
        return resumo


# Programa Principal
resp = notas(4, sit=True)
print(resp)
help(notas)