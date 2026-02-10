from time import sleep
print("-=-" * 20)
print("                 Progressão Aritimética")
print("-=-" * 20)
primtermo = int(input("Me fala o primeiro termo da progressão: "))
razao = int(input("Me fale a razão: "))
print("O resto da progressão aritimetica até o 10, é a seguinte: ")
for c in range(1, 11):
    termo = primtermo + (c -1) * razao
    sleep(0.5)
    print("termo {}: {}".format(c, termo))
print("esses são os termos")
