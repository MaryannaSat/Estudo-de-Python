print('Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.')
import random
import time
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = random.randint(0,5)

m = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')

time.sleep(3)

if m == n:
    print('PERDI! Parabéns, eu pensei mesmo no número {}.'.format(n))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n , m))

print('__FIM__')