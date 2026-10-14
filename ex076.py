cont = h = 0
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o ultimo número: "))
tot = n1, n2, n3, n4
q = (tot.count(9))
print(20 * "-=-")
print(f"Você digitou os números {tot}")
print(f"O número 9 apareceu {q} vezes")
for un, nan in enumerate(tot):
    if nan == 3:
        h = (tot.index(3))
        print(f"O 1 número 3 apareceu na posição {h + 1}")
        break
    else:
        cont += 1
        if cont == 4:
            print("Não foram digitados o Número 3")

print("Os numeros pares são: ", end="")
for pos, num in enumerate(tot):
    if num % 2 == 0:
        print(f"{num}", end = " ")
print()
print(20 * "-=-")
