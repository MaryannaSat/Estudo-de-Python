print('Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.')
def area(a,b):
    s = a*b
    print(f'A area de um terreno de {a:.2f}x{b:.2f} é de {s:.2f}m.')

print(f'Controle de Terrenos')
print('-'*35)
a = int(input(f'LARGURA (L):'))
b = int(input(f'COMPRIMENTO (C):'))
area(a,b)