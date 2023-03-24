print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto')
from datetime import date
b = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

if b == 0:
    b = date.today().year


if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
        print('Este ano é Binario ')
else:
        print('Este ano não Binario ')

