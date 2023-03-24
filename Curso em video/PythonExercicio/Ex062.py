print('Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.')

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


m = 11
f = 0
t = -1
while t != 0:
    t = int(input('Quantos termos você quer mostrar a mais?'))
    while m < t + 11:

        an = a1 + (m - 1) * r

        print(an, end=' -> ')
        m = m + 1
    print('Acabou')
    f = f + t
print('Prograssão finalizada com {} termos mostrados'.format(10+f))


