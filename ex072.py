cedula50 = cedula20 = cedula10 = cedula1 = tot1= tot2 = tot3 = tot4 = tot5 = tot6 =  0
cedula110 = cedula120 = 0
f = "Banco MAVRI"
print(50 * "-")
print(f"{f:^50}")
print(50 * "-")
while True:
    valor = int(input("Qual valor deseja sacar? R$"))
    cedula50 = valor // 50
    tot = cedula50 * 50
    tot1 = valor - tot
    cedula120 = tot1 // 20
    cedula20 = cedula120 * 20

    tot3 = tot + cedula20
    tot4 = valor - tot3
    cedula10 = tot4 // 10
    cedula110 = cedula10 * 10

    tot5 = tot3 + cedula110
    tot6 = valor - tot5
    cedula1 = tot6 // 1

    if valor % 50 == 0:
        print(50 * "=")
        print(f" Total de {cedula50} cedulas de 50 reais")
        print(50 * "=")
        break
    else:
        if tot1 % 20 == 0:
            print(50 * "=")
            print(f" Total de {cedula50} cedulas de 50 reais \n Total de {cedula120} cedulas de 20 reais")
            print(50 * "=")
            break
        else:
            if tot4 % 10 == 0:
                print(50 * "=")
                print(f" Total de {cedula50} cedulas de 50 reais\n Total de {cedula120} cedulas de 20 reais"
                      f"\n Total de {cedula10} cedulas de 10 reais")
                print(50 * "=")
                break
            else:
                if tot6 % 1 == 0:
                    print(50 * "=")
                    print(f" Total de {cedula50} de 50 reais\n Total de {cedula120} cedulas de 20 reais\n"
                          f" Total de {cedula10} cedulas de 10 reais\n Total de {cedula1} cedulas de 1 reais")
                    print(50 * "=")
                    break
print("Fim Do Saque")
