from time import sleep
print("-=-" * 20)
print("               Soma de numeros pares")
print("-=-" * 20)
valor = 0
for c in range(0, 6):
    sleep(0.2)
    numero = int(input("Me fale o {} numero: ".format(c+1)))
    if numero % 2 == 0:
        valor = valor +numero
sleep(0.5)
print("A soma dos numeros pares é {}".format(valor))
