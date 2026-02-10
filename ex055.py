import datetime
ano = datetime.date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nasc = int(input("Qual é o ano de nascimento da pessoa {}?".format(c)))
    idade = ano - (nasc)
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f"Temos {maiores} maiores de 18 anos")
print(f"Temos {menores} menores de 18 anos")

