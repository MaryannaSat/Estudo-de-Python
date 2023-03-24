print('Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')

resp = 'S'
n = 0
m = 0
c = 0
v = 0
Ma = 0
Me = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    m += n
    c += 1
    if c == 1:
        Ma = Me = n
    else:
        if n > Ma:
            Ma = n
        if n < Me:
            Me = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
v = m / c
print('Você digitou {} números e a media entre foi {}. '.format(c , v))

print('O maior valor foi {} e o menor foi {}'.format(Ma , Me))