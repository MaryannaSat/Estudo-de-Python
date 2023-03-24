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