print(' Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.')

from Ex112.utilidadescv import moeda
from Ex112.utilidadescv import dados


num = dados.leiaDinheiro('Digite um preço:R$')

moeda.Resumo(num, 20, 12)
