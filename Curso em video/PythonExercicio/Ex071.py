print('Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:\nconsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.')

print('='*30)
print('         BANCO CEV')
print('='*30)


sac = int(input('Que valor você quer sacar? R$ '))
tol = sac
cin = 50
tcin = 0
while True:
    if tol >= cin:
        tol -= cin
        tcin += 1
    else:
        print(f'Total de {tcin} células de R${cin}')
        if cin ==50:
            cin = 20
        elif cin ==20:
            cin = 10
        elif cin == 10:
            cin = 1
        tcin = 0
        if tol == 0:
            break





