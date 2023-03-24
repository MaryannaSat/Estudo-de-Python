print('Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')

C = float(input(' Temperatura atual, em Celsius:'))

F = (C * (9 / 5)) + 32

print(' A temperatura {}°C é {} em Fahrenheit.'.format( C , F))