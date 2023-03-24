print('Crie um programa que leia o nome completo de uma pessoa e mostre: \n O nome com todas as letras maiúsculas e minúsculas.\n Quantas letras ao todo ..sem considerar espaços.. .\n Quantas letras tem o primeiro nome.')

nome = str(input('Nome Completo: ')).strip()

print(nome.upper(), nome.lower())

m = len(nome) - nome.count(' ')

print(m)

'''print(nome.find(' '))'''

separar = nome.split()

print( len(separar[0]))

