print('Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.')

from datetime import date

a = int(input('Qual ano vc nasceu? '))
at = date.today().year
id = at - a

print('Quem nasceu em {} tem {} em 2020.'.format(a , id))
if id == 18:
    print('Atenção!! É hora de se alistar ao serviço militar!')

elif id < 18:
    print('Ainda falta {} anos para o alistamento \nSeu alistamento será em {}'.format(18-id , at + (18-id) ))

else:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}'.format(id-18 , at - (id-18)))


