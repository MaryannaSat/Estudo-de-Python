print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# Verifique quem é menor
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n1:
    me = n3
# Verifique quem é menor
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n1:
    ma = n3
print('O menor numero é {}'.format(me))
print('O maior numero é {}'.format(ma))