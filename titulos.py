from cores import Cores
from time import sleep


cores = Cores()


def tit(txt='Título', sim='~'):
    tam = len(txt) + 30
    print(sim * tam)
    print(txt.center(tam))
    print(sim * tam)
    print()

def tabela_opcoes():
    operacoes = ['soma/subtração', 'multiplicação', 'divisão', 'nenhuma operação']
    op = 0
    cor = [cores.azul, cores.vermelho, cores.amarelo, cores.verde]
    print('-----------------------------')
    for p in operacoes:
        print(f'{cor[op]}{op + 1}- {operacoes[op]}' + cores.fim)
        op += 1
    print('-----------------------------')
        
    sleep(2)