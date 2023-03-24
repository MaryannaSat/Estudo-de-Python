print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\n– Até 9 anos: MIRIM\n– Até 14 anos: INFANTIL\n– Até 19 anos: JÚNIOR\n– Até 25 anos: SÊNIOR\n– Acima de 25 ano0s: MASTER')
from datetime import date

a = int(input('Ano de nascimento do atleta: '))

at = date.today().year

id = at - a

print('O atleta tem {} anos'.format(id))
if id <= 9:
    print('Classificação: MIRIN!')

elif id <= 14:
    print('Classificação: INFANTIL!')

elif id <= 19:
    print('Classificação: JÚNIOR!')

elif id <= 25:
    print('Classificação: SÊNIOR!')

else:
    print('Classificação: MASTER!')
