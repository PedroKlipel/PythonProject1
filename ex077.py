compras = "Pão", 1, "Leite", 4.59, "Borracha", 0.50, "Caderno", 20.50, "Caneca", 29.90
print(50 * "-")
print("{:^50}".format("Compras Do Dia"))
print(50 * "-")
for cont, comp in enumerate(compras):
    if cont % 2 == 0:
        print("{:.<40}R$ {:>7.2f}".format(comp, compras[cont +1]))
