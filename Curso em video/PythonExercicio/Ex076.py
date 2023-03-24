print('Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.')
print('-'*30)
print('      LISTAGEM DE PREÇOS')
print('-'*30)

'''for l in c:
    if l.lower() in 'aeiou':
        print(l, end=' ')'''

p = ('Lápis', 1.75,
    'Borracha', 2.00,
     'Caderno', 15.90,
     'Estojo', 25.00,
     'Tnansferidor', 4.20)

for pos in range(0 , len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<20}', end=' ')
    else:
        print(f'R${p[pos]:.2f}')
print('-'*30)