'''
**kwargs
trabalha com dicionário
pode chamar de **x

'''

'''
def signos(**signo):
    print(signo)

signos(taty='touro', joao='áries', maria='gêmeos')
'''
'''
formas de diferente de usar a funcao com **signo
def signos(**signo):
    for nome, signo_ in signo.items():
        print(f'O signo de {nome} é {signo_}')
'''


#signos(taty='touro', joao='áries', maria='gêmeos')


def signos(*elementos, **signo):
    i = 0
    for nome, signo_ in signo.items():
        print(f'O signo de {nome} é {signo_} elemento ', elementos[0+i])
        i += 1


signos('terra', 'fogo', 'ar', taty='touro', joao='áries', maria='gêmeos')
