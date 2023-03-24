print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

P = float(input('Valor do produto? \n'))

s = P*(5/100)

d = P - s

print('O desconto foi de {:.2f} reais , logo o valor final é {:.2f} reais. '.format( s , d))