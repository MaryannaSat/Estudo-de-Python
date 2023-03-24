print(' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:\nA) qual é o total gasto na compra.\nB) quantos produtos custam mais de R$1000.\nC) qual é o nome do produto mais barato.')

print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)

t = c = b = co = 0
while True:

    no = str(input('Nome:')).upper().strip()
    pr = float(input('Preço: R$'))
    op = ' '
    co += 1
    if pr > 1000:
        c += 1
    if co == 1 or pr < b:
        b = pr
        br = no


    while op not in 'SN':

        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    t += pr

    if op == 'N':
        break


print('FIM')

print(f' O total da compra foi R${t:.2f}')
print(f'Temos {c} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {br} que R${b:.2f}')