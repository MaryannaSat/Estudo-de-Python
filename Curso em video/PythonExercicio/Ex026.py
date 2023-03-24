print('Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')

n = str(input('Escreva uma frase: ')).strip()

m = n.lower()

print('A frase tem {} As.'.format(m.count('a')))

print('O -A- parece primeiramente na posição {}.'.format(m.find('a')+1))

print('O -A- parece por último na posição {}.'.format(m.rfind('a')+1))