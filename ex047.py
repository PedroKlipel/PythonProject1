import time
print("=-=" * 30)
print("                         contagem regresiva paro o ano novo")
print("=-=" * 30)
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
time.sleep(0.5)
print("Feliz ano novo")
