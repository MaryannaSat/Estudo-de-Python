print(' Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:\nA) Quantos números foram digitados.\nB) A lista de valores, ordenada de forma decrescente.\nC) Se o valor 5 foi digitado e está ou não na lista.')
v = []
a = 1

while True:
    n = int(input('Digite um valor:'))
    v.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if op == 'N':
        break
    a += 1

v.sort(reverse=True)
print('=-'* 30)
print(f'Foram adicionados {a} valores.\nA lista dos valores da forma decrescente é {v} ')
if 5 in v:
    print(f'O 5 Está na lista ')
else:
    print(f'O 5 Não Está na lista ')

