print('Vamos criar um menu em Python, usando modularização.')

def linha(tan =42):

    return '-' * tan

def cabecalho(txt) :
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu PRiNCIPAL')
    c = 1
    for item in lista:
        print(f'{c}-{item}')
        c += 1
    print(linha())

menu([ 'Criac Arauivo', 'Cadastrac Pessoas', 'Listar Pessoas', 'Sair do Sistema'])