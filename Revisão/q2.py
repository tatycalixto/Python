listaVeiculos = ['fusca', 'gol', 'uno', 'vectra', 'palio']
listaConsumo = [7, 10, 12.5, 9, 14.2]
consumo = list()
print('Comparativo de Consumo de Combustível')
print('-='*25)
print('Veículo\t\tNome\t\tKm/litro' + '\n')
for i in range(5):
    print("%s\t\t%s\t\t%.2f" %
          (str(i+1), listaVeiculos[i], listaConsumo[i]))
print('-='*25)
print("Relatório Final\n")
for i in range(5):
    litros = 1000/listaConsumo[i]
    consumo.append(litros*4.93)
    print(i+1, '-', listaVeiculos[i], '-', listaConsumo[i],
          '- ', "%.2f" % litros, ' litros', ' - R$ ', "%.2f" % consumo[i])
menor = min(consumo)
m_pos = consumo.index(menor)
print('O menor consumo é do ', listaVeiculos[m_pos])
