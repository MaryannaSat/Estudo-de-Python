print('Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:\nAPOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.')

frase = str(input('Digite uma frase:')).strip().upper()

pal = frase.split()

junto = ''.join(pal)
inverso = junto[::-1]

'''inv = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')

