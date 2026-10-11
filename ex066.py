menor = 0
maior = 0
tot = 0
cont = 0
media = 0
continuar = "S"
while continuar == "S":
    valor = int(input("Me fale um número: "))
    continuar = str(input("Deseja continuar? [S/N]")).upper()
    cont += 1
    if cont == 1:
        menor = valor
        maior = valor
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    tot += valor

media = tot / cont
print(f"O maior valor digitado é {maior}, \n"
      f"o menor valor digitado é {menor}, \n"
      f"a média dos valores são {media}")
