'''def soma(a,b):
    s = a + b
    print(s)

#Programa Principal
soma(2,2)
soma(5,3)'''

'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = s')

#Programa Principal
soma(2,2)'''
#desapacotar
'''def contador(* num):
    for valor in num:
        print(valor, end=' ')
    print('Fim')


# Programa Principal
contador(2,1,3)
contador(2,3,4,5)'''

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao do tamanho {tam}')


# Programa Principal
contador(2,1,3)
contador(2,3,4,5)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1,2,3,1]
dobra(valores)
print(valores)
