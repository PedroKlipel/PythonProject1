s = 0
print("=-=" * 35)
print("                        Números multiplos somados de 3 do 1 até o 500")
print("=-=" * 35)
for c in range(0, 501):
    if c % 3 == 0 and c % 2 == 1:
        s = s + c
print(s)
