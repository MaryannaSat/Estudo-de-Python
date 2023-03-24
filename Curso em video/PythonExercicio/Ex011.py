print( 'Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de        tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')

l = float(input('Largura da parede em metro:'))

h = float(input('Altura da parede em metro:'))

area = l*h

tinta = area / 2

print('Parede tem {} m^2 de área e será necessario {} litros para pintar a parede toda.'.format( area , tinta))