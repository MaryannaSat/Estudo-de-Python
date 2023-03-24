print('Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.')


def ajuda(con):
    help(con)

def titulo(msg):
    tam = len(msg) + 4
    print('~~' * tam)
    print(f'{msg}')
    print('~~' * tam)

#
comando = ''
while True:
    titulo('SISTEMA DA AJUDA PYTHON')
    comando = str(input('Função da biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até LOGO')