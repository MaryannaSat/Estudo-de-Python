print('Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:\n5! = 5 x 4 x 3 x 2 x 1 = 120')

n = int(input('Escolha um número:'))

m = n
f = 1
while m > 0:

    print('{}'.format(m), end='')
    print('x' if m > 1 else '=', end='')
    f = f * m
    m = m - 1

print(f)