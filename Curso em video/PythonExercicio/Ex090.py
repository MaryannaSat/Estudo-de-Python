print('Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.')

dados = dict()

dados['nome'] = str(input('Nome:'))
dados['média'] = float(input(f'Media de {dados["nome"]}:'))
print('-='*40)
for r,v in dados.items():
    print(f'- {r} é igual a {v}.')
if dados['média'] <= 5:
    print('- situação é igual a Reprovado.')
else:
    print('- situação é igual a Aprovado.')