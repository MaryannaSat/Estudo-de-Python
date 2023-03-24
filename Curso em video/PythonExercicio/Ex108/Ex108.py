print('Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.')

import moeda

num = float(input('Digite um preço:R$'))

print(f'O preço foi de {moeda.moeda(num)} para {moeda.moeda(moeda.aumentar(num,10))}.')

print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')

print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')