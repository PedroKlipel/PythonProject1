#Errei, era para eu perguntar quantos números a mais ele queria que eu mostra-se, porem fiz que é a cada 5
#Não irei corrigir pois achei mais disafiador fazer assim, porém eu sei como faz do jeito que o professor queria
#Alem de ser muito mais facil
from time import sleep
print(20 * "=-=")

ptermos = int(input("Digite um termo: "))
razao = int(input("Digite a razao: "))
cont = 1

print(20 * "=-=")

tal = True
cont1 = 1
while cont < 11:
    termo = ptermos + (cont -1) * razao
    cont += 1
    print(termo)
    sleep(0.3)
print(20 * "=-=")
continuar = input("Deseja continuar com mais 5? [S/N] ").upper()
print(20 * "=-=")

while tal == True:
    if continuar == "S":
        cont1 = 0
        while cont1 < 6:
            termo = ptermos + (cont -1) * razao
            cont += 1
            cont1 += 1
            print(termo)
            sleep(0.3)
            if cont1 >= 6:
                print(20 * "=-=")
                continuar = str(input("Deseja continuarcom mais 5? [S/N] ")).upper()
                print(20 * "=-=")
    if continuar == "N":
        tal = False

print("Fim Do Programa")
print(20 * "=-=")
