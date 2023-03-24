print(' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:\na) de 1 até 10, de 1 em 1\nb) de 10 até 0, de 2 em 2\nc) uma contagem personalizada')

from time import sleep

def contador(i,f,p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('-='*35)
    print(f'Contage de {i} até {f} é {p} em {p}')
    cont = 1

    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.1)
            cont -= p
        print('FIM')
        print('-=' * 35)
    else:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.1)
        print('FIM')
        print('-=' * 35)



#Pricipal Comando
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contaem!')
i = int(input('Início:'))
f = int(input('FIM:'))
p = int(input('Passo:'))

contador(i,f,p)