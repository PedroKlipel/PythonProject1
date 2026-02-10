numero = int(input("Me fale um numero: "))
primo = True
for c in range(2, numero):
    if numero % c == 0:
        primo = False
if primo and numero > 1:
    print(f"o numero {numero} é primo")
else:
    print(f"o numero {numero} não é primo")
