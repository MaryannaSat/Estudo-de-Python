print('Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.')

t = int(input('Escolha uma tabuada? '))
print('='*20)
print('Tabuada do {}'.format(t))
print('='*20)
for c in range(1,10):
    print('{}X{}={}'.format(t , c , t*c))
print('Fim')