n1 = float(input("digite sua primeira nota do bimestre: "))
n2 = float(input("digite sua segunda nota do bimestre: "))
media = (n1 + n2) / 2
if media < 5:
    print("você está de \033[0;31mREPROVOU\033[m pois sua media é de \033[0;31m{:.1f}".format(media))
elif 5 <= media < 6.9:
    print("Você esta de \033[0;33mRECUPERAÇÃO\033[m pois sua nota é de \033[0;33m{:.1f}".format(media))
else:
    print("Você está \033[1;32mAPROVADO\033[m parabens")