ano = int(input("me fale o ano que vc está"))
if ano % 4 == 0:
    if ano % 400 == 0:
        print("o ano {} é um ano bissexto".format(ano))
    else:
        print("o ano {} não é um ano bissexto".format(ano))
else:
    print("o ano {} não é um ano bissexto".format(ano))
