from time import sleep
print("=-=" * 20)
print("                        tabuada")
print("=-=" * 20)
sleep(0.3)
num = int(input("Me fale um número"))
print("A taubuda de {} até o 10 é:".format(num))
for c in range(0, 11):
    tabu = num * c
    sleep(0.5)
    print("{} Vezes {} = {}".format(num, c, tabu))
print("Aqui está a tabuada :)")
