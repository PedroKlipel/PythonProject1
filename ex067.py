cont = s = 0
while True:
    n = int(input("Me fale qualquer número (999 para parar): "))
    if n == 999:
        break
    else:
        s += n
        cont += 1
print(f"Você digitou {cont} vezes, e a soma de tudo é igual {s}")
