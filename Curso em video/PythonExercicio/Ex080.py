print('Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.')

v = []

for cont in range(0,5):
    n = int(input('Adicionar:'))
    if cont == 0 or n > v[-1]:
        v.append(n)
    else:
        pos = 0
        while pos < len(v):
            if n <= v[pos]:
                v.insert(pos, n)
                break
            pos += 1
print(v)


'''        if v[cont] > a:
            a = v[cont]
        elif v[cont] < menor:
            menor = v[cont]'''