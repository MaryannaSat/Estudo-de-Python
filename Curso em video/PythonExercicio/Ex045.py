print('Crie um programa que faça o computador jogar Jokenpô com você.')
import time
from random import randint

alt = randint(1,3)

print('+-'*30)
print('Vamos jogar Jokenpô!')
print('+-'*30)
time.sleep(2)
op = int(input('Escolhe a opção \n[1]PEDRA \n[2]PAPEL \n[3]Tesoura:'))

print('='*30)
print('Jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('pô!')
time.sleep(1)
print('='*30)




if op == 1:
    if alt == 2:
        print('Você jogou Pedra e eu sou PAPEL!')
        print('Vc PERDEU ;)')
    elif alt == 3:
        print('Você jogou Pedra e eu sou TESOURA!')
        print('Vc GANHOU :(')
    elif alt == 1:
        print('Você jogou Pedra e eu sou PEDRA!')
        print('EMPATOU')

elif op == 2:
    if alt == 1:
        print('Você jogou PAPEL e eu sou PEDRA!')
        print('Vc GANHOU :(')

    elif alt == 2:
        print('Você jogou PAPEL e eu sou PAPEL!')
        print('EMPATOU')
    elif alt == 3:
        print('Você jogou PAPEL e eu sou TESOURA!')
        print('Vc PERDEU ;)')
elif op == 3:
    if  alt == 1:
        print('Você jogou TESOURA e eu sou PEDRA!')
        print('Vc PERDEU ;)')
    elif alt == 2:
        print('Você jogou TESOURA e eu sou PAPEL!')
        print('Vc GANHOU :(')
    elif alt == 3:
        print('Você jogou TESOURA e eu sou TESOURA!')
        print('EMPATOU')

else:
    print('Ops, só existe IMPAR ou PAR, opção INCORRETA!')