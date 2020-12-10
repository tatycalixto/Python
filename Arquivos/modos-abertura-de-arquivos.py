'''
modos de abertura
x-> abre para escrita apenas se o arquivo não existir
a-> abre para escrita adicionando o conteúdo no final do arquivo
#obs: se o arquivo não existir ele será criado se já existir
será adicionado no final
+-> abre para o modo de atualização (leitura e escrita)
'''
'''
with open('universidade.txt', 'x', encoding='utf8') as arquivo:
    arquivo.write('teste de conteúdo.\n')
'''

'''
#escreve no final do arquivo

'''
with open('frutas.txt', 'a', encoding='utf8') as arquivo:
    while True:
        fruta = str(input("Informe uma fruta ou digite sair: "))
        if fruta != 'sair':
            arquivo.write(fruta+'\n')
        else:
            break
