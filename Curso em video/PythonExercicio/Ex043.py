print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:\n– IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida')

p = float(input('Peso do paciente:'))
h = float(input('Altura do paciente:'))

imc = p / (h*h)

print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')

elif imc <= 25:
    print('Peso Ideal!')

elif imc <= 30:
    print('Sobrepeso!')

elif imc <= 40:
    print('Obesidade!')

else:
    print('Obesidade Mórbida!')