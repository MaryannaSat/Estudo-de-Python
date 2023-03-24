print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')

s = float(input('Qual é o salário do funcionário? '))

if s <= 1250:

    a = s + (s * 10 / 100)

    print(' Quem ganha R${:.2f} passa a ganhar R${:.2f} agora!'.format(s,a))
else:
    a = s + (s * 15 / 100)

    print(' Quem ganha R${:.2f} passa a ganhar R${:.2f} agora!'.format(s, a))

