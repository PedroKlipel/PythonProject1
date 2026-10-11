ptermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
cont = 1
while cont < 11:
    termo = ptermo + (cont -1 ) * razao
    cont += 1
    print(termo)
print("Essa é a PA")
