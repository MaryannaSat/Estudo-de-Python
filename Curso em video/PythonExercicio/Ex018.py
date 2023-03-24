import math

print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')

A = float(input('Difite o ângulo que você deseja:'))

sen = math.sin(math.radians(A))

cos = math.cos(math.radians(A))

tan = math.tan(math.radians(A))

print('O ângulo de {:.1f} tem seno de {:.2f}, cosseno de {:.2f} e a tangente de {:.2f}.'.format(A , sen , cos , tan))