ptermos = int(input("Digite um termo: "))
razao = int(input("Digite a razao: "))
cont = 1
tal = True
cont1 = 1
while cont < 11:
    termo = ptermos + (cont -1) * razao
    cont += 1
    print(termo)
continuar = input("Deseja continuar com mais 5? [S/N] ").upper()

while tal == True:
    if continuar == "S":
        cont1 = 0
        while cont1 < 6:
            termo = ptermos + (cont -1) * razao
            cont += 1
            cont1 += 1
            print(termo)
            if cont1 >= 6:
                continuar = str(input("Deseja continuarcom mais 5? [S/N] ")).upper()
    if continuar == "N":
        tal = False

