'''
Escrevendo em arquivos
#abrir o arquivo em modo write (escrita)
#Obs:quando abrimos um arquivo  para leitura, não
# podemos realizar a escrita nele. Apenas ler.
# Da mesma forma, se abrirmos um arquivo para escrita 
não podemos ler, apenas escrever.

obs: se adicionar novos dados ele sobrescreve (perde tudooo!)

'''
# modo de arquivo w (write)
# ao abrir um arquivo para escrita o arquivo é criado no SO
with open('novo.txt', 'w', encoding='utf8') as arquivo:
    arquivo.write('outro Teste escrita de arquivo\n')
    arquivo.write('Outra linha aqui 123\n')
    arquivo.write(' última linha 123\n')
'''

'''


'''
escrever um número x de vezes uma string
with open('texto.txt', 'w', encoding='utf8') as arquivo:
    arquivo.write('Python\n'*100)

'''

'''
Dados inseridos pelo teclado


'''
with open('frutas.txt', 'w', encoding='utf8') as arquivo:
    while True:
        fruta = str(input("Informe uma fruta ou digite sair: "))
        if fruta != 'sair':
            arquivo.write(fruta+'\n')
        else:
            break
