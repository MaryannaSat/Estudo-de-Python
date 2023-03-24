print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')
dado = []
turma = []
nota = []
while True:
    dado.append(str(input('Nome:')))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    m = (n1 + n2)/2
    dado.append(m)
    nota.append(n1)
    nota.append(n2)
    dado.append(nota[:])
    turma.append(dado[:])
    dado.clear()
    nota.clear()

    op = str(input('Que continuar? [S/N]')).upper().strip()[0]
    if op in 'N':
        break

print('-='*40)

print('No. NOME        MÉDIA')
print('-'*30)
for i, j in enumerate(turma):
    print(f'{i}  {j[0]}       {j[1]}')

while True:
    ma = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if ma == 999:
        break
    else:
        print(f'Nota de {turma[ma][0]} são {turma[ma][2]}.')
'''ficha = list()

nome = str('Nome')
n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
m = (n1+n2)/2
ficha.append([nome, [n1,n2], m])

print()'''