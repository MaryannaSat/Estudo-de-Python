print('Crie um programa que faça o computador jogar Jokenpô com você.')
import time
from random import randint

alt = randint(1,10)

print('+-'*30)
print('Vamos jogar111!')
print('+-'*30)
time.sleep(2)
op = int(input('Escolhe a opção \n[1]Impar \n[2]Par:'))

print('='*30)
print('Jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('pô!')
time.sleep(1)
print('='*30)

v = int(input('Qual é sua jogada:'))

print('A minha foi:{}'.format(alt))

j = v + alt


if op == 1:
    print('Deu {} . Você escolheu IMPAR e eu sou PAR!'.format(j))
    print('Vc PERDEU ;)')
elif op == 1 and (j%2) == 1:
    print('Deu {} . Você escolheu IMPAR e eu sou PAR!'.format(j))
    print('Vc GANHOU :(')
elif op == 2 and (j%2) == 1:
    print('Deu {} . Você escolheu PAR e eu sou IMPAR!'.format(j))
    print('Vc PERDEU ;)')
elif op == 2 and (j%2) == 0:
    print('Deu {} . Você escolheu PAR e eu sou IMPAR!'.format(j))
    print('Vc GANHOU :(')
else:
    print('Ops, só existe IMPAR ou PAR, opção INCORRETA!')