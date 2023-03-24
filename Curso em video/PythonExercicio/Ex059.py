print('Crie um programa que leia dois valores e mostre um menu na tela:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nSeu programa deverá realizar a operação solicitada em cada caso.')

n1 = int(input('Primeiro valor:'))

n2 = int(input('Segundo valor:'))

print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')

op = 0
while op != 5:
    op = int(input('Qual é a sua opção?'))
    if op == 1:
        print('Somando os dois números:{}'.format(n1 + n2))
    elif op == 2:
        print('Multiplicação os dois números:{}'.format(n1 * n2))
    elif op == 3:
        if n1 > n2:
            m = n1
            print('Maior dos dois números:{}'.format(m))
        else:
            m = n2
            print('Maior dos dois números:{}'.format(m))

    elif op == 4:
        print('Informe números novos:')
    else:
        print('Opção Incorreta')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')

print('Final')