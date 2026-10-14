frases = "Perna", "Brasil", "Bahia", "Casca", "Mordida", "Quarto", "Segredo", "Casa", "Mouse", "Celular"
cont = cont1 = 0
silabas = "a", "e", "i", "o", "u"
for palavras in frases:
    cont = 0
    print(f"As silabas da palavra {palavras.upper()} são:", end="")
    for letra in palavras:
        if letra in silabas:
            cont += 1
            print(f" {letra}", end="")
    print()
