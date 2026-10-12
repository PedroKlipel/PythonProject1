cont = vezes = 0
while True:
    print("=-=" * 20)
    n = int(input("Qual tabuada vc quer saber? "))
    print("=-=" * 20)
    if n < 0:
        break
    else:
        cont = 1
        while cont < 11:
            print(f"{n} x {cont} = {n * cont}")
            cont += 1
print("Fim")
