from math import trunc

print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.')

num = float(input('Digite um numero?'))

int = trunc(num)

print(' O numero digitado é {} e sua porção inteira é {}.'.format(num , int))

