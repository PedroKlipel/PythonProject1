lista = []
listaP = []
listaI = []
while True:
    n = int(input("Digite um numero: "))
    continuar = 'Jesus'
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    lista.append(n)
    if continuar == 'N':
        break
for i in lista:
    if i % 2 == 0:
        listaP.append(i)
    else:
        listaI.append(i)
print("=-=" * 20)
print(f"O resultado da lista é {lista}\nO resultado da lista par é {listaP}"
      f"\nO resultado da lista impar é {listaI}")
