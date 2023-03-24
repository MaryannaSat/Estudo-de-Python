print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.')

n = str(input('Qual é o seu nome? ')).strip()

m = n.upper()

print('Existe Silva no nome? {}'.format('SILVA' in m))

