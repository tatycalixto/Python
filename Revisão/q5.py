import random


def embaralhar(palavra):
    nova_palavra = ""
    nova_palavra = random.sample(
        palavra.lower(), len(palavra))  # retorna uma lista aleatória
    print('A palavra que você digitou invertida fica com join: ',
          ''.join(nova_palavra))
    # converter um lista em strings
    print('A palavra que você digitou invertida fica: ', nova_palavra)


embaralhar("PYTHON")
