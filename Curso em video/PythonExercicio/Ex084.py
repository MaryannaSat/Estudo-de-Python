print('Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:\nA) Quantas pessoas foram cadastradas.\nB) Uma listagem com as pessoas mais pesadas.\nC) Uma listagem com as pessoas mais leves.')


dados = list()
pn = list()
P = list()

min = mai = 0
p = 0
while True:

    pn.append(str(input('Qual é o seu nome? ')))
    pn.append(int(input('Qual é o seu peso?')))
    if len(dados) == 0:
        mai = min = pn[1]
    else:
        if pn[1] > mai:
            mai = pn[1]
        if pn[1] < min:
            min = pn[1]
    dados.append(pn[:])
    pn.clear()

    p += 1
    op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if op in 'N':
        break




print(f'Foi cadastrado {p} pessoas.')#ou len(dados)

print(f'O maior peso é {mai}. Peso:', end='')
for p in dados:
    if p[1] == mai:
        print(f'{p[0]}')
print()
print(f'O menor peso {min}. Peso:', end='')
for p in dados:
    if p[1] == min:
        print(f'{p[0]}', end='')
print()


