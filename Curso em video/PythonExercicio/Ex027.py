print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')

n = str(input('Qual é o seu nome Completo? '))

m = n.split()

p = len(m)

print('Seu primeiro nome é {}'.format(m[0]))

print('Seu ultimo nome é {}'.format(m[len(m)-1]))
