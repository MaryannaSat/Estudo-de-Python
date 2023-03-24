print(' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.')

def ficha(n=0, g=0):

    if n == '':
        return f'O jogador <desconhecido> fez {g} gols no capeonato.'
    else:
        return f'O jogador {n} fez {g} gols no capeonato.'

n = str(input('Nome do Jogador:'))
g = str(input('Numero de Gols:'))

if g.isnumeric():
    g = int(g)
else:
    g = 0
print(ficha(n,g))

