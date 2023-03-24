print('Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.')

print('='*20)
print('10 TERMOS DE PA')
print('='*20)

a1 = int(input('Primeiro termo: '))

r = int(input('Razão: '))

n = 1
while n < 11:
    an = a1 + (n - 1) * r

    print(an, end=' -> ')
    n = n + 1
print('Acabou')
