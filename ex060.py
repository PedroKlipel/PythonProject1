n1 = int(input("digite um número inteiro qualquer: "))
n2 = int(input("digite outro número inteiro qualquer: "))
opcao = 0
while opcao != 5:
    print(20 * "-=-")
    print(" [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair")
    opcao = int(input("Digite a Opção: "))
    if opcao == 1:
        print(f"A soma entre {n1} + {n2} = {n1 + n2}")
    elif opcao == 2:
        print(f"A multiplicação entre {n1} * {n2} = {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número entre {n1} e {n2} é o {n1}")
        else:
            print(f"O maior número entre {n1} e {n2} é o {n2}")
    elif opcao == 4:
        n1 = int(input("Digite um número inteiro qualquer: "))
        n2 = int(input("Digite um númeto inteiro qualquer: "))
print("Acabou")
