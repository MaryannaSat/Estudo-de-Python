print('Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.')

n = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:\n [ 1 ] converter para BINARIO\n [ 2 ] converter para OCTAL\n [ 3 ] coverter para HEXADECIMAL')

op = int(input('Sua opção:'))

if op == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n , bin(n)[2:]))
elif op == 2:
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))

elif op == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))

else:
    print('Codigo invalido!')