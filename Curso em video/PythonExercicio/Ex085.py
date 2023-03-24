print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.')
dados = [[], []]
op = 0
for p in range(1,8):
    op = int(input(f'Digite {p}° valor: '))
    if op % 2 == 0:
        dados[0].append(op)
    else:
        dados[1].append(op)


print(dados)
dados[0].sort()
dados[1].sort()
print('='*35)
print(f'Os valores pares digitados foram: {dados[0]}')
print(f'Os valores ímpares digitados foram: {dados[1]}')