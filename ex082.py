lista = []
while True:
    n = int(input('Digite um numero: '))
    continuar = "Joelmo"
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista.append(n)
    if continuar == 'N':
        break
print("=-=" * 20)
print(f"Você digitou {len(lista)} numeros ")
print(f"Os valores em ordem descresente são {sorted(lista, reverse=True)}")
if 5 in lista:
    print(f"Achei o numero 5 na posição: {lista.index(5) + 1} ")
else:
    print("O número 5 não foi encontrado")
