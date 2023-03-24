print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.')

v = []
p = []
i = []

while True:
    n = int(input('Digite um valor:'))
    v.append(n)


    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)

    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if op in 'Nn':
        break

print('=+'*30)
print(f'A lista completa é {v}')
print(f'A lista com os impares é {i}')
print(f'A lista com os pares é {p}')