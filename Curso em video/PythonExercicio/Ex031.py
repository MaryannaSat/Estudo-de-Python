print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas')

d = float(input('Qual é a Distancia da sua viagem do carro?'))

if d < 200:

    p = d * 0.5

    print(' Voce esta prestes a começar uma viagem de {:.1f}Km.\n E o preço da sua passagem será de R${:.2f}!'.format(d,p))
else:
    p = d * 0.45

    print(' Voce esta prestes a começar uma viagem de {:.1f}Km.\n E o preço da sua passagem será de R${:.2f}!'.format(d,p))


print('Boa viagem!!')
