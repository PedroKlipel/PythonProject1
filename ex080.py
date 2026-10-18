lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        print("Valor adicionado na lista.")
        lista.append(n)
    else:
        print("Valor duplicado. Não irei adicionar.")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
lista.sort()
print(f"Você digitou os valores {lista}")
