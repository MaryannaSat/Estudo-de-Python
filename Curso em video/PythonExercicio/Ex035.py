print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')