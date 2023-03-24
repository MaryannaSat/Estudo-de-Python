print('Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.')

import moeda

num = float(input('Digite um preço:R$'))

print(f'O preço foi de {num} para {moeda.aumentar(num,10)}.')

print(f'A metade de {num} é {moeda.metade(num)}')

print(f'O dobro de {num} é {moeda.dobro(num)}')