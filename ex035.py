salario = float(input("Digite o seu salario: "))
if salario >= 1250:
    aumento = salario * (10 / 100)
    print("O seu salario será de {}".format(salario + aumento))
if salario < 1250:
    aumento = salario * (15 / 100)
    print("Os seu salario será de {}".format(salario + aumento))
