# listaSituacao = [0]*4
soma = 0
dicioSituacao = {'1': [0, 'Necessita da Esfera'], '2': [0, 'Necessita de limpeza'], '3': [
    0, 'Necessita de troca'], '4': [0, 'Quebrado         ']}
print('-='*20)
print("Digite 0 para encerrar a entrada de dados.")
print('-='*20)
situacao = input(
    "Digite a situação do mouse:\n 1- Necessita da Esfera\n 2- Necessita de limpeza\n 3- Necessita de troca\n 4-Quebrado        \n")
soma = 0
while situacao != '0':
    for k, v in dicioSituacao.items():

        if situacao in k:
            dicioSituacao[k][0] = v[0]+1
            # print("dicio: ", dicioSituacao[k][0])
            # soma = dicioSituacao[k][0]
            # print("Soma dento do if: ", soma)
    situacao = input(
        "Digite a situação do mouse:\n 1- Necessita da Esfera\n 2- Necessita de limpeza\n 3- Necessita de troca\n 4-Quebrado\n")
for k, v in dicioSituacao.items():
    soma += dicioSituacao[k][0]
print("Quantidade de mouses: ", soma)
print("Situação\t\t\tQuantidade\t\tPercentual")
for k, v in dicioSituacao.items():
    print(f"{k}-"+str(dicioSituacao[k][1])+"\t\t\t"+str(dicioSituacao[k][0])+"\t\t"
          + str((dicioSituacao[k][0]*100)/soma)+"%")
