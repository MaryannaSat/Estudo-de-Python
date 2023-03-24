def aumentar(n=0,taxa=0, formato=False):

    v = n +(n * taxa/100)
    return v if formato is False else moeda(v)


def diminuir(n=0,taxa=0, formato=False):

    v = n - (n * taxa / 100)
    return v if formato is False else moeda(v)


def dobro(n=0, formato=False):

    return n*2 if formato is False else moeda(n*2)

def metade(n=0, formato=False):

    return n/2 if formato is False else moeda(n/2)

def moeda(n = 0, moeda = ' R$'):
    return f'{moeda}{n:>8.2f}'.replace('.', ',')


def Resumo(n, aumenta, reduzir):

    print("-" * 30)
    print('Resumo do Valor'.center(30))
    print("-" * 30)
    print(f'Preço analisado: \t\tR${n:.2f}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t\tR${n/2:.2f}')
    print(f'{aumenta}% de aumento: \t{aumentar(n, aumenta,True)}')
    print(f'{reduzir}% de aumento: \t{diminuir(n, reduzir, True)}')
    print("-" * 30)
