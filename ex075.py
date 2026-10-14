from random import randint
cont = maior = menor = 0
t = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
for numeros in (t):
    cont += 1
    if cont == 1:
        maior = numeros
        menor = numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
print(f"Os números sorteados foram {t}")
print(f"O menor valor foi {menor} e o maior foi {maior}")
