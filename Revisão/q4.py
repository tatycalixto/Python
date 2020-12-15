listaTemperatura = list()
listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for i in range(12):
    listaTemperatura.append(
        float(input("Digite a temperatura do mês "+str(i+1)+" : ")))

media = sum(listaTemperatura)/len(listaTemperatura)
print("-="*20)
print("A média anual das temperaturas: ", "%.2f" % media, "ºC")
print("-="*20)
for i in range(12):
    if listaTemperatura[i] > media:
        print("Temperatura acima da média ",
              listaTemperatura[i], "ºC", listaMeses[i])
