print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.')
Peso = 0
peso = 0
for c in range(1 , 6):
    p = float(input('Digite o peso da {}° pessoa?:'.format(c)))
    if c == 1:

        Peso = c
        peso = c
    else:
        if p > Peso:
            Peso = p
        if p < peso:
            peso = p

print('O maio peso é {:.1f}'.format(Peso))
print('O menor peso é {:.1f}'.format(peso))



