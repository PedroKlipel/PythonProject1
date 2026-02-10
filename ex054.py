frase = input("Digite uma frase: ").upper().strip()
espaço = frase.split()
junto = ''.join(espaço)
inver = ""
for c in range(len(junto)-1, -1, -1):
    inver += junto[c]
if inver == junto:
    print("A palavra {} é um polindromo".format(inver.lower()))
else:
    print("A palavra {} não é um polindromo".format(frase.lower()))