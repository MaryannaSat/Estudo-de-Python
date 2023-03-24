print('Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:\nA) Quantas vezes apareceu o valor 9.\nB) Em que posição foi digitado o primeiro valor 3.\nC) Quais foram os números pares.')

n = (int(input('Digite um número:')), int(input('Digite um número:')), int(input('Digite um número:')), int(input('Digite um número:')))

print(f'Você digitou os valores {n}.')
print(f'Aparece {n.count(9)} vezes o nove.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os números pares são ', end='')
for par in n:
    if par % 2 == 0:
        print(par, end=' ')

