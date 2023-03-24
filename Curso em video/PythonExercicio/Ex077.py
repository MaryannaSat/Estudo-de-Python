print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.')

p = ('cadeiras', 'mesa', 'celular')

for c in p:
    print(f'\nA palavra {c} temos', end='' )
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')