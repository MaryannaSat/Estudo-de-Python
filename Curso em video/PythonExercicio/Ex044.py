print('Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:\n– à vista dinheiro/cheque: 10% de desconto\n– à vista no cartão: 5% de desconto\n– em até 2x no cartão: preço formal \n– 3x ou mais no cartão: 20% de juros')

v = float(input('Valor do produto: R$ '))

f = int(input('Forma de pagar:  \n[1]Dinheiro/Cheque(À vista) \n[2]Cartão(À vista) \n[3]Cartão(até 2X) \n[4]Cartão(3X ou mais) '))

if f == 1:
    print('Valor a ser pago no total é de R${:.2f}.'.format(v - (v*10/100)))

elif f == 2:
    print('Valor a ser pago no total é de R${:.2f}.'.format(v - (v * 5 / 100)))

elif f == 3:
    p = int(input('Quantas parcelas? '))
    print('Valor a ser pago no total é de R${:.2f} e será parcelado em {}x de R${:.2f}.'.format(v , p , v/p))
elif f == 4:
    p = int(input('Quantas parcelas? '))
    print('Valor a ser pago no total é de R${:.2f} e será parcelado em {}x de R${:.2f}.'.format(v + (v * 20 / 100) , p , (v + (v * 20 / 100) )/p))
else:
    print('Forma de pagamento INCORRETA')