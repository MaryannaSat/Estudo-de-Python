print('Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: \nA) Quantas pessoas foram cadastradas \nB) A média de idade \nC) Uma lista com as mulheres \nD) Uma lista de pessoas com idade acima da média')

from datetime import datetime

pe = dict()
l = list()
s = list()

c = m = 0

while True:
    pe['nome'] = str(input('Digite seu nome:'))
    while True:
        pe['sexo'] = str(input('Digige o sexo [F/H]:')).upper().strip()[0]
        if pe['sexo'] not in 'FfHh':
            del pe['sexo']
            print(f'Erro! Por favor, digite apenas M ou F.')
        else:
            break
    pe['ano de nascimento'] = int(input('Digige seu ano de nascimento:'))
    pe['idade'] = datetime.now().year - pe['ano de nascimento']

    c += 1
    m += pe['idade']

    if pe['sexo'] in 'Ff':
        s.append(pe['nome'])
    pe['mulher'] = s


    l.append(pe.copy())


    while True:
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
            break
        print(f'Erro! Por favor, digite apenas S ou N.')
    if op == 'N':
        break

print('=-'*35)

print(l)
print(f'Ao todo temos {c} pessoas cadastradas.')
print(f'A média de idade é de {m/c} anos.')
print(f'As mulheres cadastradas foram', end=' ')
for h in s:
    print(f'{h}', end=' ')
print()
print(f'Lista das pessoas que estão acima da média:')
if pe['idade'] > 40:
    del pe['mulher']
    del pe['ano de nascimento']
    for t in l:
        for k, v in pe.items():
            print(f'{k} = {v};', end=' ')
        print()
print()
print('<< ENCERRADO >>')