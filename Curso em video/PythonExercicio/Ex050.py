print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.')

cost=0

for c in range(1 ,7):
    p = int(input('Escolha um número? '))
    if p%2 == 0:
        cost += p

print('Somado da {}'.format(cost))