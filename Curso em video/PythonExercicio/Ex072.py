print('Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

while True:
    nu = int(input('Escolha um número entre 0 e 20:'))
    if 0<= nu <= 20:
        break
    print('Tente novamente.', end=' ')

print(f'Você digitou o número {numero[nu]}.')