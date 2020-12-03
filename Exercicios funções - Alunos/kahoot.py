def funcaoEnigma3(n):
    soma = 0
    for i in range(1, n+1):
        soma = soma+i
    j = 1
    while j <= n:
        soma = soma-j
        j = j+1
    return soma


# print(funcaoEnigma3(2))

def funcaoEnigma4(n):
    mult = 1.0
    i = 0
    while i <= n-2:
        mult = mult*((i+1.0)/(i+2.0))
        i = i+1
    return mult*n


# print(funcaoEnigma4(50))

def funcao3(frase):
    contador = 0
    k = 0
    while k < len(frase)/2:
        if frase[k] == " ":
            contador = contador+1
        print(contador)


#funcao3('um dois tres')
def funcao4(frase):
    nova_frase = ''
    k = 0
    while k < len(frase):
        nova_frase = frase[k] + nova_frase + frase[k]
        k = k+1
    print(nova_frase)


# funcao4('54321')
def funcao1(lista):
    temp1 = lista[0]
    temp2 = lista[len(lista)-1]
    for elemento in lista:
        if temp1 > elemento:
            temp1 = elemento
        if temp2 < elemento:
            temp2 = elemento
    print(str(temp1) + ' ' + str(temp2))


lista = [1, 2, 4, 16, 32, 64, -128]
funcao1(lista)
