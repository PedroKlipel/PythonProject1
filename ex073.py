ext = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
       "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    n = int(input("Digite um número de 0 a 20: "))
    while n not in range(0, 21):
        n = int(input("Tente novamente, Digite um número de 0 a 20: "))
    len(ext)
    print(f"Você digitou o numero, {ext[n]}")
    break
print("{:-^20}".format("Fim do Programa"))
