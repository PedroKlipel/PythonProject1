menor = 0
maior = 0
for i in range (0, 5):
    peso = int(input(f"digite o peso da pessoa {1 + i}: "))
    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(menor)
print(maior)
