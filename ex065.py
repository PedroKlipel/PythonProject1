num1 = 0
cont = 0
tot = 0
while num1 != 999:
    num1 = int(input("Digite um número de 0 a 999: "))
    if num1 != 999:
        cont += 1
        tot += num1
print(f"Você digitou {cont} antes de cancelar,"
      f" a soma de todos os números é {tot} ")
