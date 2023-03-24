print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')

salario = float(input('Qual é o seu salário? \n R$'))

aumento = salario * (15 / 100)

final = aumento + salario

print(' Seu salário atual é de R${:.2f} e aumento foi de R${:.2f}, logo o seu novo salário é de R${:.2f}.'.format( salario , aumento , final))