print('Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.')
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(1,6):
        lista.append(randint(0,9))
    for v in num:
        print(v, end=' ')
        sleep(0.5)
    print('Pronto')


def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos', end=' ')
    c = 0
    for v in num:
        if v % 2 == 0:
            c += v
        sleep(0.2)
    print(c)
    sleep(0.2)


num = list()

sorteia(num)
somaPar(num)


