from time import sleep
print(23 * "=-=")
n = int(input("Me fale quantas vezes vc quer ver a sequência de Fibonacci: "))
print(23 * "=-=")
n1 = 0
m1 = 0
m3 = 1
while n1 < n:
    sleep(0.3)
    print(m1)
    fn = m1 + m3
    m1 = m3
    m3 = fn
    n1 += 1
print(28 * "=-=")
print(f"Esta é a sequencia de fibonacci, aparecendo apenas {n} desta sequencia")
print(28 * "=-=")
