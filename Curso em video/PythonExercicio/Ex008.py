print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')

n = float(input('\nDigite o valor que quer converter de metro para centímetro e milímetros. \n'))

cm = n * 100

mm = n * 1000

print(' O valor de {} metros é {} centímetro e {} milímetro.'.format(n , cm , mm))