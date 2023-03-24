print('Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.\nEx:\nescreva(‘Olá, Mundo!’) Saída:\n~~~~~~~~~\nOlá, Mundo!\n~~~~~~~~~')

def escrever(msg):
    tam = len(msg)
    print('~'* tam)
    print(msg)
    print('~'* tam)


#Programa Principal
escrever('Oiii')