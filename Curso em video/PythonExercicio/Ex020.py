from random import shuffle
print('O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

a1 = str(input('Aluno 1:'))]


a2 = str(input('Aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
lista = (a1 , a2 , a3 , a4)

shuffle(lista)

print('A ordem é ')
print(lista)
