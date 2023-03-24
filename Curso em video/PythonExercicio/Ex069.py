print('Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:\nA) quantas pessoas tem mais de 18 anos.\nB) quantos homens foram cadastrados.\nC) quantas mulheres tem menos de 20 anos.')
s = f = 0
c = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    id = int(input('Idade:'))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo:[M/F]')).upper().strip()[0]

    if id >= 18:
        c += 1

    if sx == 'M':
        s += 1

    if sx == 'F' and id < 20:
        f += 1

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if op == 'N':
        break


print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao todo temos {s} homens cadastrados')
print(f'E temos {f} mulheres com menos de 20 anos')