n1 = int(input("Me fale um número qualquer: "))
n2 = n1
n3 = 1
while n2 != 0:
    n3 = n3 * n2
    n2 -= 1
print(f"O número factorial é {n3}")
