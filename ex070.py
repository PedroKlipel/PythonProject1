from time import sleep
continuar = "S"
m = sexo1 = pessoas = 0
while True:
    if continuar == "S":
        print(20 * "=-=")
        idade = int(input("Digite sua idade: "))
        sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if idade > 18:
            pessoas += 1
        else:
            pessoas += 0
        if sexo == "M":
            sexo1 += 1
        if sexo == "F" and idade < 20:
            m += 1
    else:
        break
sleep(0.5)
print(20 * "=-=")
print(f" Temos {pessoas} pessoas maiores de 18 anos \n Temos {sexo1} homens cadastrados "
      f"\n Temos {m} mulheres/meninas menores de 20 anos")
