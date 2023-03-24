print(' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.')

import random

n = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print(f'Os valores sorteados foram:', end=' ')
for nu in n:
    print(f'{nu}', end=' ')

print(f'\nO maior valor sorteado foi {max(n)}.')

print(f'O maior valor sorteado foi {min(n)}.')


