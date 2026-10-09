sexo = "J"
while sexo != "M" and sexo != "F":
    sexo = str(input("Digite seu sexo: ")).strip().upper()
if sexo == "M":
    print("Você é um Homem")
else:
    print("Você é uma Mulher")