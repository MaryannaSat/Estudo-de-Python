print('Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.')

j = dict()
gols = list()

j['Nome do jogador'] = str(input('Digite o nome do jogador:'))
p = int(input('Digite a quantidades de partidas:'))
tot = 1
c = 0
while tot <= p:
    g = int(input(f'Digite a quantidades de gols {tot}:'))
    gols.append(g)
    tot += 1
    c += g

j['Gols'] = gols
j['total'] = c

print('=-'*30)
print(j)
print('=-'*30)
for k, v in j.items():
    print(f'O campo {k} tem o valor {v}. ')
print('=-'*30)

print(f'O {j["Nome do jogador"]} jogou {p} partidas')

for m, n in enumerate(gols):
    print(f'=> N partida {m+1}, fez {n} gols. ')
print(f'Foi um total de {c} gols.')
print('=-'*30)
