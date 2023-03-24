print('Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.')
from random import randint

print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)
jogos = []
lista = []
tot = 1
op = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= op:
    cont = 0
    while True:
         al = randint(1, 60)
         if al not in lista:
            lista.append(al)
            cont +=1
         if cont >= 6:
             break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os numeros sorteados foram:.')
for p, c in enumerate(jogos):
    print(f'Jogo {p} ={c}')


