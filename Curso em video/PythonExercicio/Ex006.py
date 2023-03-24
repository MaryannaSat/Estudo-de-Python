print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

n = float(input('Digite um número. \n'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro, triplo e a raiz de {} é {}, {} e {}, respectivamente.'.format(n , d , t , r ))