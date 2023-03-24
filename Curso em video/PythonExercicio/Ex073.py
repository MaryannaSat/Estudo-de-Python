print('Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:\na) Os 5 primeiros times.\nb) Os últimos 4 colocados.\nc) Times em ordem alfabética.\nd) Em que posição está o time da Chapecoense.')

brasileirao = ('São Paulo', 'Flamengo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Ceará SC', 'Atlético-GO', 'Athletico-PR', 'Bragantino', 'Fortaleza', 'Sport', 'Bahia', 'Vasco', 'Botafogo', 'Coritiba', 'Goiás')

print(f'Lista de times do Brasileirão:{brasileirao}')

print(f'Os 5 primeiros são {brasileirao[0:6]}')

print(f'Os 4 últimos são {brasileirao[15:]}')

print(f'Times em ordem alfabética{sorted(brasileirao)}')

print(f'O Chapecoente está na {brasileirao.index("São Paulo")+1}° posição')