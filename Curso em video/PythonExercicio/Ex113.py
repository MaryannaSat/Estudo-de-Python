print('Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('Erro! diite um valor certo')
            continue
        except (KeyboardInterrupt):
            print('Erro!! espaço')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('Erro! diite um valor certo')
            continue
        except (KeyboardInterrupt):
            print('Erro!! espaço')
            return 0
        else:
            return n



#Programa principal
n = leiaInt('Digite um numero: ')
p = leiafloat('Digite um:')
print(f'Voce acabou de digitar o numero {n}\n {p}')

