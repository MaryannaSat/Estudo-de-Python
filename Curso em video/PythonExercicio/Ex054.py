print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')

from datetime import date

at = date.today().year

cont1 = 0
cont2 = 0
for c in range(1 , 8):
    n = int(input('Digite ano de nascimento da {}° pessoa?:'.format(c)))
    id = at - n
    if id < 21:
        cont1 += 1

    else:
        cont2 += 1

print('Ao todo tivemos  {} pessoas maiores de idade\nE também tivemos {} pessoas menor de idade'.format(cont2 , cont1))

print('\033[33m', end=' ')