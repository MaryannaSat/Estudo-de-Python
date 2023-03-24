print('Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')

from datetime import datetime

dados = list()
aluno = dict()

aluno['nome'] = str(input('Digite seu nome:'))
aluno['ano de nascimento'] = int(input('Digige seu ano de nascimento:'))
aluno['CTPS'] = int(input('Digige sua carteira de trabalho:( 0 não tem)'))
aluno['idade'] = datetime.now().year - aluno['ano de nascimento']
dados.append(aluno)

if aluno['CTPS'] > 0:
    aluno['ano de contratação'] = int(input('Digige seu ano de contratação:'))
    aluno['salário'] = int(input('Digige seu salário:'))
    aluno['aposentadoria'] = ((aluno['ano de contratação'] + 35) - datetime.now().year) + aluno['idade']
    for k, v in aluno.items():
        print(f'- {k} tem o valor {v}')

else:
    del aluno['carteira']
    for k, v in aluno.items():
        print(f'- {k} tem o valor {v}')
