import random
numero = random.randint(1, 10)
n = 11
tentativa = 0
print("Escolhi um número de 1 a 10, tente adivinhar")
while n != numero:
    n = int(input("Digite um numero entre 1 e 10: "))
    tentativa += 1
print(f"Parabéns, você acertou, você tentou {tentativa} vezes")
