cont = cont2 = erro = erro1 = 0
eq = str(input("Digite a equação: "))
lista = []
lista.append(eq)
for i in lista:
    for carac in i:
        if carac == "(":
            cont += 1
        if carac == ")":
            cont2 += 1
        if cont2 - cont == 1:
            erro += 1

if erro > 0:
    print("Não é valido")
    erro1 += 1
if erro1 < 1:
    if cont != cont2:
        print("Não é valido")
    if cont == cont2:
        print("É valido")
