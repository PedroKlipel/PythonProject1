barato = ""
total = caro = barato2 = cont = 0
continuar = "S"
f = "mercadinho muito legal"
print(25 * "--")
print(f"{f:^50}")
print(25 * "--")
while True:
    if continuar == "S":
        cont += 1
        nome = str(input("Digite o nome do produto: "))
        preco = float(input("Digite o valor do produto: R$"))
        continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        while continuar not in "SN":
            continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
        if cont == 1:
            barato2 = preco
            barato = nome
        if preco < barato2:
            barato = nome
        if preco > 1000:
            caro += 1
        total += preco
    else:
        break
f2 = "Resumo da Compra"
print(f"{f2:-^50}")
print("")
print(f"O total da compra foi de R${total:.2f}, \n"
      f"o produto mais barato foi o {barato}, \n"
      f"e teve {caro} produtos acima de R$1000.00")
