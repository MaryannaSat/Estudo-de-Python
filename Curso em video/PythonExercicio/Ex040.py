print('Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:\n– Média abaixo de 5.0: REPROVADO\n– Média entre 5.0 e 6.9: RECUPERAÇÃO\n– Média 7.0 ou superior: APROVADO')


n1 = float(input('Nota 1? '))
n2 = float(input('Nota 2? '))

m = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1 , n2 , m))
if m < 5.0:
    print('Reprovado!!')

elif 5.0 <= m <= 6.9:
    print('Recuperação')

else:
    print('Aprovado')
