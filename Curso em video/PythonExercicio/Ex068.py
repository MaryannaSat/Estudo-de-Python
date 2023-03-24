print('Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')

import random

'''print('+-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('+-'*30)

p = 'Pp'
i = 'Ii'
lista = [p , i]

s = random.randint(1,100)
p = random.choice(lista)

c = 0
while True:
    n = int(input('Diga um valor:'))
    p = str(input('Par ou impar? [P/I]')).upper().strip()[0]
    so = n + s
    if so%2 == 0:
        if p == 'Pp':
            print('-' * 30)
            print(f' Você; jogou {n} e o computador {s}. Total de {so} Deu PAR')
            print('Você VENCEU!')
            print('-' * 30)
        elif p == 'Ii':
            print('-' * 30)
            print(f' Você. jogou {n} e o computador {s}. Total de {so} Deu PAR')
            print('Você PERDEU!')
            print('-' * 30)
            break
    elif so%2 == 1:
        if p == 'Ii':
            print('-' * 30)
            print(f' Você.. jogou {n} e o computador {s}. Total de {so} Deu IMPAR')
            print('Você VENCEU!')
            print('-' * 30)
        elif p == 'Pp':
            print('-' * 30)
            print(f' Você;; jogou {n} e o computador {s}. Total de {so} Deu IMPAR')
            print('Você PERDEU!')
            print('-' * 30)
            break
    c+= 1
print(f'GAME OVER! Você venceu {c} ')'''

from random import randint


v = 0
while True:
    n = int(input('Diga um valor:'))
    s = randint(0, 10)
    so = n + s
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).upper().strip()[0]
    print(f' Você jogou {n} e o computador {s}. Total de {so}')
    print('DEU PAR' if so % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if so % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if so % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print()

