print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.')

print('='*20)
print('10 TERMOS DE PA')
print('='*20)

a1 = int(input('Primeiro termo: '))

r = int(input('Razão: '))



for n in range(1 , 11):

     an = a1 + (n - 1) * r

     print(an, end=' -> ')
print('Acabou')



'''r = an - an-1'''
