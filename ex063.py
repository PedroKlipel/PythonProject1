ptermos = int(input("Digite um termo: "))
razao = int(input("Digite a razao: "))
cont = 1
while cont < 11:
    termo = ptermos + (cont -1) * razao
    cont += 1
    print(termo)
continuar = input("Deseja continuar com mais 5? [S/N] ").upper()

if continuar == "S":
    cont = 1
    while cont < 6:
        termo = ptermos + (cont -1) * razao
        cont += 1
        print(termo)

