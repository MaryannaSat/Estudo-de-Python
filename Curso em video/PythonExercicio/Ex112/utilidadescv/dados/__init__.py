def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrda = str(input(msg))
        if entrada.islpha():
            print(f'Erro! \"{entrda}\" é um preço invalidp!')
        else:
            valido= True
            return float(entrda)