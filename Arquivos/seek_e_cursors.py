'''
a função seek é usada para movimentar o cursor no arquivo

readline - leitura linha a linha
readlines - ler tudo colocando cada linha como um item de 
uma lista de strings

OBS: quando criamos um arquivo função open() é criada uma conexão
entre o arquivo no disco do PC e o nosso programa. Essa conexão
e´chamada de streaming. Ao finalizar devemos fechar 
a conexão e para isso usamos a função close
'''

# arquivo com acento
arquivo = open('teste.txt', encoding='utf8')
'''
print(arquivo.read())

# movimentando o cursor pelo arquivo com a função seek

'''
# arquivo.seek(0)  # volta o cursor na posição 0
# print(arquivo.read())

# readline
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(linha)
linhas = arquivo.readlines()
#tamanho = len(linhas)
for i in range(0, len(linhas)):
    if i > 0 and i < 3:
        print(linhas[i])

# print(len(linhas))
# print(arquivo.readlines())
# readlines
# print(arquivo.readlines())
# print(linhas)
# print(arquivo.closed) # verifica se um arquivo está aberto ou fechado
# fechar arquivo
# arquivo.close()
# print(arquivo.closed)  # verifica se um arquivo está aberto ou fechado
