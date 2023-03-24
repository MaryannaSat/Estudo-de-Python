print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.')

n = str(input('Nome do aluno:'))

n1 = float(input('Qual é a nota da Prova 1? \n'))

n2 = float(input('Qual é a nota da Prova 2? \n'))

m = (n1 + n2)/2

print(' A média do(a) {} é {:.1f} .'.format(n , m))
