coloca = ("Flamengo", "Palmeiras", "Athletico-PR", "Fluminense", "Bahia", "Cruzeiro", "Atlético-MG",
          "Santos", "Red Bull Bragantino", "São Paulo", "Coritiba", "Vitória", "Botafogo",
          "Vasco da Gama", "Mirassol", "Corinthians", "Internacional", "Grêmio", "Remo", "Chapecoense")
print("-=-" * 20)
print(f" Os times do Brasileirão são: {coloca}")
print("-=-" * 20)
print(f"Os primeiros 5 colocados são: {coloca[:5]}")
print("-=-" * 20)
print(f"Os 4 ultimos colocados são: {coloca[16:]}")
print("-=-" * 20)
print(f"O times em ordem alfabetica são: {sorted(coloca)}")
print("-=-" * 20)
for pos, times in enumerate(coloca):
    if times == "Chapecoense":
        print(f"O Chapecoense está na {pos + 1} colocação")
