lanche = ('h', 's', 'p', 'pu')
print(lanche[1:3])#s e p

'''for comida in lanche:
    print(f'{comida}')'''

'''for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont+1}')'''

'''for pos,comida in enumerate(lanche):
    print(f'{comida} na posição {pos+1}')'''

'''print(sorted(lanche))#organizar
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))#quantas vezes apareceu 5
print(c.index(4))#qual a posição está o 4
del(b)#apagar a variavel(não posso apagar so um elemento)
