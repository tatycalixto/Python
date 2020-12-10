'''
bloco with
check list para usar arquivo
  #1- Abrimos o arquivo
  #2- Manipulamos o arquivo
  #3- Fechamos o arquivo

#with - é a forma mais usada para se trabalhar
#com  arquivos em python
'''
# bloco with (abre e fecha o arquivo)

with open('teste.txt', encoding='utf8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


# print(arquivo.closed)
