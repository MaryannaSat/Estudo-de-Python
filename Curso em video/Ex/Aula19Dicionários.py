'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade': 22}

#print(f'O {pessoas["nome"]}, tem {pessoas["idade"]} anos')
pessoas['peso'] = 55#adicinar
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'São paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado2)
brasil.append(estado1)
print(brasil)'''

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federalidade:'))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')