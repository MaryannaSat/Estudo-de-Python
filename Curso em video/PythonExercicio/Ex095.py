print('Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.')

time = list()
pt = list()

while True:
    j = dict()
    gols = list()
    j['Nome do jogador'] = str(input('Digite o nome do jogador:'))
    p = int(input('Digite a quantidades de partidas:'))
    tot = 1
    c = 0
    while tot <= p:
        g = int(input(f'Digite a quantidades de gols na partida {tot}:'))
        gols.append(g)
        tot += 1
        c += g

    for m, n in enumerate(gols):
        print(f'=> N partida {m + 1}, fez {n} gols. ')
    print(f'Foi um total de {c} gols.')

    j['Gols'] = gols
    j['total'] = c
    j['partidas'] = p
    pt.append(p)
    print('=-'*30)
    print(j)
    print('=-'*30)


    time.append(j.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
            break
        print(f'Erro! Por favor, digite apenas S ou N.')
    if op == 'N':
        break
print('=-'*30)
del j['partidas']
print(f'cod. ', end=' ')
for k in j.keys():
    print(f'{k:>12}', end=' ')
print()
print('-'*60)
for i in range(0, len(time)):
    print(f' {i}    {time[i]["Nome do jogador"]}     {time[i]["Gols"]}       {time[i]["total"]}  ')

while True:
    ma = int(input('Mostrar gols de qual jogador? (999 interrompe):'))
    if ma == 999:
        break
    else:
        for z in range(0, pt[ma]):
            print(f'=> Na partida {z+1} foi {time[ma]["Gols"][z]} gols.')




