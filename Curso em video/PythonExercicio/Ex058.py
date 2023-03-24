print('Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.')

import random
import time
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
n = random.randint(0,10)



time.sleep(2)

c = 0
m = 1
while m != n:

    m = int(input('Em que número eu pensei? '))

    print('PROCESSANDO...')
    time.sleep(2)
    if m == n:
        print('PERDI! Parabéns, eu pensei mesmo no número {}.'.format(n))

    else:
        print('GANHEI! Eu pensei não no {}! Tente de novo'.format(m))
        c += 1

print('Precisou de {} vezes para você ganhar!'.format(c))
print('__FIM__')