lista = []
cont =0
while cont < 5:
    n = int(input("Digite um valor: "))
    cont += 1
    if cont == 1:
        lista.append(n)
    for pos, numero in enumerate(lista):
        if n < numero:
            lista.insert(pos, n)
            break
    if cont > 1:
        if n >= numero:
            lista.append(n)
print(lista)
