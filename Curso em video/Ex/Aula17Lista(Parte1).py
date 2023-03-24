n = [2, 5, 9, 1]
n[2] = 3
n.append(7)
n.sort(reverse=True)
n.insert(2, 2)
n.remove(2)

print(n)

valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)
'''
for cont in range(0,5):
    valores.append(int(input('Adicionar:')))
'''for v in valores:
    print(f'.{v}...', end=' ')'''

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrase o valor {v}')

print('Fim')