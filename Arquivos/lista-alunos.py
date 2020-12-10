def dados():
    lista_Alun = list()
    lista_Alun_Composta = list()
    qntd_Alunos = 0
    i = 0
    media = 0
    aluno = -1
    qntd_Alunos = int(input('Quantos(as) Alunos(as)?'))
    for q in range(0, qntd_Alunos):
        lista_Alun.append(str(input('Digite o nome do(a) aluno(a): ')))
        lista_Alun.append(float(input('Digite a primeira nota ')))
        lista_Alun.append(float(input('Digite a segunda nota ')))
        media = (float(lista_Alun[i+1])+float(lista_Alun[i+2]))/2
        lista_Alun.append(float(media))
        # print(lista_Alun)
        lista_Alun_Composta.append(lista_Alun[i:])
        i += 4
    gravar_Dados(lista_Alun_Composta)


# criando  a tabela no arquivo
def gravar_Dados(lista_Alun_Composta):
    i = 0
    with open('alunos.txt', 'a', encoding='utf8') as arquivo:
        arquivo.write('#'*30+'\n')
        arquivo.write("Nome\t\tMédia"+'\n')

        for a in range(0, len(lista_Alun_Composta)):
            arquivo.write("%s\t\t%.2f" %
                          (lista_Alun_Composta[a][i], lista_Alun_Composta[a][3]))
            arquivo.write('\n')
        arquivo.write('#'*30)

dados()

