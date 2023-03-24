print('Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.')

from time import sleep

def maior(* num):
    print('-=' * 35)
    print('Analisando os valores passados...')
    cont = ma = menor = 0
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.1)
        if cont == 0:
            ma = menor = n
        else:
            if n > ma:
                ma = n
            elif n < menor:
                menor = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {ma}')
    print('-=' * 35)

maior(2,2,2,2,3)