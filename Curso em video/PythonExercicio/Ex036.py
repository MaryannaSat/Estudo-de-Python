print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')

v = float(input('Valor da casa? '))

s = float(input('Valor do salario do comprador? '))

a = int(input('Quantos anos vai pagar? '))

p = v / (a * 12)

if p <= (s * 30 /100 ):
    print('Emprestimo Aprovado!')

else:
    print('Emprestimo NEGADO!!')