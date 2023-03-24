print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.')

c = 1
while c != 'M' and c != 'F':
    c = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

print('FIM')