lista = []
maior = menor = cont = 0
for hj in (range(5)):
    lista.append(int(input(f"Me fale um valor para a posição {hj}: ")))
    if hj == 0:
        maior = lista[0]
        menor = lista[0]
    if lista[hj] > maior:
        maior = lista[hj]
    if lista[hj] < menor:
        menor = lista[hj]

print("-=-" * 20)
print(f"O maior valor digitado foi: {maior} na posição ", end="")
for c, v in enumerate(lista):
    if v == maior:
        cont += 1
        print(c, end=" e " if lista.count(maior) - 1 == cont else "" if lista.count(maior) == cont else ", ")
print()
print(f"O menor valor digitado foi: {menor} na posição ", end="")
cont = 0
for c, v in enumerate(lista):
    if v == menor:
        cont += 1
        print(c, end=" e " if lista.count(menor) - 1 == cont else "" if lista.count(menor) == cont else ", ")
print()
print("-=-" * 20)
