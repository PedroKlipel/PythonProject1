from random import randint
frase = "Par ou Impar" #bah meu, podia fazer isso sem precisar criar uma variavel ein
print(f"{frase:^50}")
cont = 0
while True:
    print(20 * "=-=")
    n = int(input("Escolha um numero: "))
    modo = str(input("Escolha uma opcao [P|I]: ")).upper().strip()[0]
    print(20 * "=-=")
    com = randint(1, 10)
    s = n + com
    if modo == "P":
        if s % 2 == 0:
            print("Você ganhou")
            print(f"Escolhi o número {com}")
            cont += 1
        else:
            break
    if modo == "I":
        if s % 2 == 1:
            print("Você ganhou")
            print(f"Escolhi o número {com}")
            cont += 1
        else:
            break
print(f"Você perdeu, tu ganhou {cont} vezes")
print(f"Escolhi o número {com}")
