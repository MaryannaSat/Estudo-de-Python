print('Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:\n– EQUILÁTERO: todos os lados iguais\n– ISÓSCELES: dois lados iguais, um diferente\n– ESCALENO: todos os lados diferentes')

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')

    elif l1 == l2 or l1 == l3 :

        print('ISÓSCELES!')

    else:
        print('ESCALENO!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')

