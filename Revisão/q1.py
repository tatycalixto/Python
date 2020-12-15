salarios = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699],
            [700, 799], [800, 899], [900, 999]]
faixa = [0]*9
print("Faixa Início: ", faixa)

print("Digite 0 para encerrar a entrada de dados.")
vendas = int(input("Digite o valor das vendas:"))

while vendas != 0:
    salario = (vendas*9)/100+200
    if salario < 1000:
        for i in range(8):
            if salario > salarios[i][0] and salario < salarios[i][1]:
                faixa[i] += 1
    else:
        faixa[8] += 1
        # print(faixa[8])
    vendas = int(input("Digite o valor das vendas:"))
print('-='*20)
for i in range(8):
    print("Entre R$", salarios[i][0], "e R$", salarios[i]
          [1], ":", faixa[i], "vendedores.")
print("Salarios maiores que R$1000:", faixa[8], "vendedores.")
print('-='*20)
print("Faixa Final: ", faixa)
