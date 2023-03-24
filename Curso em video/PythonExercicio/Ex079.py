print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.')
v = list()
c = valor = 0
while True:

    n = int(input('Digite um valor:'))
    if n not in v:
        v.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Numero duplicado')



    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if op == 'N':
        break

v.sort()
print(v)