print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')

v = []
maior = menor = 0
for cont in range(0,5):
    v.append(int(input(f'Digite um valor {cont}:')))
    if cont == 0:
        maior = menor = v[cont]
    else:
        if v[cont] > maior:
            maior = v[cont]
        elif v[cont] < menor:
            menor = v[cont]


'''while True:
    if v[0]
'''
print('-='*40)
print(f'Voce digitou os valores {v}')
print(f'O maior Valor é {maior} na posição {v.index(maior)}', end='')
for i,ve in enumerate(v):
    if ve == maior:
        print(f'{i}...', end='')
print()
print(f'O menor Valor é {menor} na posição {v.index(menor)}', end='')
for i,ve in enumerate(v):
    if ve == menor:
        print(f'{i}...', end='')
print()