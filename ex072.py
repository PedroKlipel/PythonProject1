cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    valor = int(input("Qual valor deseja sacar? R$"))
    cedula50 = valor // 50
    cedula20 = valor // 20
    cedula10 = valor // 10
    cedula1 = valor // 1
    if valor % 50 == 0:
        print(f"Total de {cedula50} cedulas de 50 reais")
        break
    else:
        tot = cedula50 * 50
        tot1 = valor - tot
        if tot1 % 20 == 0:
            print(f"Total de {cedula50} cedulas de 50 reais, \n e  {cedula20} cedulas de 20 reais")
            break
        else:
            tot3 = tot1 + tot
            tot4 = valor - tot3
            if tot4 % 10 == 0:
                print(f"Total de {cedula50} de 50 reais, \n {cedula20} de 20 reais, e \n {cedula10} de 10 reais")
                break
            else:
                tot4 = tot3 + tot4
                tot5 = valor - tot4
                if tot5 % 1 == 0:
                    print(cedula1)
                    break


