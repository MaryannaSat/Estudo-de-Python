import math

print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')

CO = float(input('Comprimento do cateto oposto:'))

CA = float(input('Comprimento do cateto adjacentes:'))

H = math.hypot(CO , CA)

'''H = math.sqrt( math.pow(CO , 2) + math.pow(CA , 2))'''

print('A hipotenusa é {:.2f}.'.format(H))