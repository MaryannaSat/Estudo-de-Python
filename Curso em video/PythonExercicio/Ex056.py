print(' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.')

me = 0
mt = 0
velho = 0
nova = 0
nome = ''
for c in range(1 , 5):
    n = str(input('Digite o nome da {}° pessoa?:'.format(c)))

    id = int(input('Digite a idade da {}° pessoa?:'.format(c)))

    s = str(input('Digite o sexo da {}° pessoa? [M/F] :'.format(c))).strip()

    mt += id

    if s == 'M':
        if c == 1:
            velho = id
            nome = n
        else:
            if id > velho:
                velho = id
                nome = n

    elif s == 'F':
        if id <= 20:
            nova += 1
    else:
        print('Erro de entrada!')



print( 'A média de idade do grupo é de {} anos'.format(mt/4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(nova))
