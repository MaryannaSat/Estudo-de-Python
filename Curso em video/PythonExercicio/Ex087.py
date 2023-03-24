print('Aprimore o desafio anterior, mostrando no final:\nA) A soma de todos os valores pares digitados.\nB) A soma dos valores da terceira coluna.\nC) O maior valor da segunda linha.')

mz = [[], [], [], []]

p = lista1 = lista2 = lista3 = k = o = q = z = 0
me = ma = 0
for o in range(1, 4):
    linha1 = int(input(f'Digite m1{o}:'))
    mz[0].append(linha1)

    if linha1 % 2 == 0:
        p += linha1
    if o == 3:
        k += linha1

for q in range(1, 4):
    linha2 = int(input(f'Digite m2{q}:'))
    mz[1].append(linha2)

    if linha2 % 2 == 0:
        p += linha2

    if q == 0:
        ma = me = linha2
    else:

        if linha2 > ma:
            ma = linha2
        elif linha2 < me:
            me = linha2
    if q == 3:
        k += linha2

for z in range(1, 4):
    linha3 = int(input(f'Digite m3{z}:'))
    mz[2].append(linha3)

    if linha3 % 2 == 0:
        p += linha3
    if z == 3:
        k += linha3

print('|', end=' ')
for v in mz[0]:
    print(f'{v}', end=' ')
print('|', end=' ')
print(' ')
print('|', end=' ')
for c in mz[1]:
    print(f'{c}', end=' ')
print('|', end=' ')
print(' ')
print('|', end=' ')
for b in mz[2]:
    print(f'{b}', end=' ')
print('|', end=' ')
print(' ')
print(f'A soma dos valores pares {p}.')
print(f'A soma dos valores da terceira coluna é {k}.')
print(f'O maior valor da segunda linha é {ma}.')