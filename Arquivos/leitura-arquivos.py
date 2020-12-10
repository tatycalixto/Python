'''
Leitura de Arquivos
r=leitura(read)
w=escrita (write)
UTF-8: todos os acentos serão reconhecidos
enconding: a codificação que o conteúdo 
do arquivo foi escrito ou deve ser lido

'''
#arquivo = open('teste.txt')
# print(arquivo.read())


# leitura de arquivo
# a função read lê todo conteúdo do arquivo
# print(arquivo.read())
arquivo = open('teste.txt', encoding='utf8')
print(arquivo.read(6))
