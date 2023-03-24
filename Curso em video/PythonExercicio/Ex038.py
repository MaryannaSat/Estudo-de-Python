print('Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:')

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print('O primeiro número é maior!')

elif n1 < n2:
    print('O Segundo número é maior!')

else:
    print('Números iguais!')
