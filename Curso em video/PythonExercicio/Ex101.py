print('Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.')

def voto(ano):
    from datetime import date
    id = date.today().year - ano
    n = 'Não Vota'
    v = 'Voto Obrigatorio'
    o = 'Voto Opcional'
    if id < 16:
        return f'Com {id} anos: Não vota'
    elif 16 <= id <18 or id > 65:
        return f'Com {id} anos: Voto opcional'
    else:
        return f'Com {id} anos: Voto obrigatorio'


print('-'*35)
ano = int(input('Em que ano vc nasceu:'))

print(voto(ano))

