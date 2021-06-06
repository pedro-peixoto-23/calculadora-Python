# Objetivo: criar uma calculadora simples, em que seja possível fazer operações 
# com mais de um valor e também com diferentes operações, usando a linguagem 
# python, no qual será executada pelo terminal


from cores import Cores
import os
from titulos import tit, tabela_opcoes
from time import sleep


cores = Cores()


def iniciar():
    lista = list()

    tit('Calculadora Automática')
    tabela_opcoes()

    verificar_o_que_o_usuario_deseja(lista)


def verificar_o_que_o_usuario_deseja(numeros):
    b = input('\nInsira o que deseja: ')

    # Se quando chamar o método for verdadeiro (True), ele passa, se não, ele 
    # mostra um erro e o ciclo ocorre novamente
    if verificar_operacao(b, numeros):
        pass

    else:
        print('🔴' + cores.vermelho + 'TENTE NOVAMENTE!' + cores.fim +
              '🔴' + '\n')
        verificar_o_que_o_usuario_deseja(numeros)


def verificar_operacao(resposta, lista):
    # Verificando qual a operação que o usuário deseja realizar
    try:
        if resposta in ('+', '-', 'somar', 'subtrair', '1'):
            inserir_valores(lista)
            somar(lista)
            return True

        elif resposta in ('*', 'x', 'multiplicar', '2'):
            inserir_valores(lista)
            mult(lista)
            return True

        elif resposta in ('/', 'dividir', '3'):
            inserir_valores(lista)
            div(lista)
            return True

        elif resposta == '4':
            verificar_reinicio()
            return True
    except:
        print('Tente novamente! Ocorreu um erro!')
        # passando a variável resposta pois ela tem a lista que será usada 
        # posteriormente
        verificar_o_que_o_usuario_deseja(resposta)


def inserir_valores(lista):
    contador = 1
    sleep(1)
    quantidade_valores = int(input(f'{cores.azul}Quantos valores você irá '
                                   'utilizar? ' + cores.fim))
    print()
    print('-----------------------------')
    while quantidade_valores != 0:
        try:
            if quantidade_valores == 1:
                valor_usuario = input(f'Último valor: ')
            else:
                valor_usuario = input(f'{contador}° valor: ')
            valor_usuario = float(valor_usuario)
            lista.append(valor_usuario)
            contador += 1
            quantidade_valores -= 1
        except:
            print(cores.vermelho + 'Ocorreu um erro, tente novamente' +
                  cores.fim)
    print('-----------------------------')


# Serve tanto para somar quanto para subtrair
def somar(lista):
    r = 0

    for p in lista:
        r += p

    print(f'O valor da (soma ou subtração), é de: {r}')
    verificar(r)


def mult(lista):
    r = 1

    for p in lista:
        r *= p

    if type(r) == float:
        print('O valor da multiplicação, é de: {:.0f}'.format(r))
    else:
        print(f'O valor da multiplicação, é de: {r}')

    verificar(r)


def div(lista):
    r = 0

    for p in lista:
        if p == lista[0]:
            # caso seja o primeiro, não precisa fazer nada
            r = p
        else:
            r /= p

    if type(r) == float:
        print('O valor da divisão, é de: {:.2f}'.format(r))
    else:
        print(f'O valor da divisão, é de: {r}')

    verificar(r)


def verificar(resultado):
    a = input(f'\n{cores.amarelo}O que você quer fazer com o resultado? ')
    print(cores.fim, end='')
    # criando uma lista para novamente fazer os cálculos
    numeros = list()
    # inserindo o resultado na lista, para ser o primeiro dela
    numeros.append(resultado)

    if verificar_operacao(a, numeros):
        pass

    elif a in ('nada', '4', 'n', 'mais nada', 'não'):
        verificar_reinicio()

    else:
        print(cores.vermelho + 
              'Digite "6", caso não queira realizar nenhuma operação!' +
              cores.fim)
        verificar(resultado)


def verificar_reinicio():
    b = input('\nDeseja iniciar novamente? (s/n) ')

    if b in ('s', 'sim'):
        os.system("cls")
        iniciar()
    else:
        print('\n' + '=' * 25 + 'Calculadora finalizada!' + '=' * 25)


os.system("cls")
iniciar()
