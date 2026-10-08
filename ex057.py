nome = ""
velho = 0
total = 0
menos = 0
for i in range(4):
    nome1 = str(input(f"digite o nome da pessoa{1 + i}: "))
    sexo1 = str(input(f"digite o sexo da pessoa{1 + i}(M OU F): ")).upper()
    idade1 = int(input(f"digite a idade da pessoa{1 + i}: "))
    if sexo1 == "M":
        if idade1 > velho:
            velho = idade1
            nome = nome1
    if sexo1 == "F":
        if idade1 < 20:
            menos += 1
    total = total + idade1

media = total / 4
print(f"Tem {menos}meninas/mulheres menores de 20 anos")
print(f"O nome do Homem mais velho é {nome}")
print(f"a idade média é de {media}")
