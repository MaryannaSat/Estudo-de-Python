print(' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:\n– Quantidade de notas\n– A maior nota\n– A menor nota\n– A média da turma\n– A situação (opcional)')

def notas(*num, sit=False):
    aluno = dict()
    t = ma = menor = cont = m = 0
    for v in num:
        if cont == 0:
            ma = menor = v
        else:
            if v > ma:
                ma = v
            elif v < menor:
                menor = v
        t += 1
        m += v

    aluno['total'] = t
    aluno['maior'] = ma
    aluno['menor'] = menor
    aluno['media'] = m/t
    if sit:
        if aluno['media'] > 7:
            aluno['stuação'] = 'Boa'
        else:
            aluno['stuação'] = 'Ruim'

    return aluno

print(notas(9,9,1))

