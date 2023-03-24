print('Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.')

mz = [[], [], []]

for p in range(1, 4):
    linha1 = int(input(f'Digite m1{p}:'))
    mz[0].append(linha1)

for q in range(1, 4):
    linha2 = int(input(f'Digite m2{q}:'))
    mz[1].append(linha2)

for z in range(1, 4):
    linha3 = int(input(f'Digite m3{z}:'))
    mz[2].append(linha3)

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

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''