saldo = [1000, 1000]

moedas = ["NitCoin", "Elitium", "NyanCoin"]
valorM = [4.53, 20.83, 10.03]
valorIn = [0, 0, 0]

sorte = [1, -1, 1]
v = [0, 0, 0]

i = 0


def esperar():
    z = 0
    for _ in valorM:
        valorM[z] = valorM[z] + sorte[z]
        z += 1

    z = 0
    for _ in range(len(sorte)):
        if sorte[z] >= 1:
            v[z] = 0

        elif sorte[z] <= -1:
            v[z] = 1

        if v[z] == 1:
            sorte[z] += 0.2
        elif v[z] == 0:
            sorte[z] -= 0.1

        z += 1


def minvest(saldo):
    while True:
        y = 0
        print("--------------------\n-----Mercado Cripto------\n--------------------\n")

        print(f"Seu saldo é R${saldo[i]}\nMoedas:")

        for _ in range(len(moedas)):
            if sorte[y] < 0:
                c = "↓"
            elif sorte[y] > 0:
                c = "↑"

            print(f"[{y+1}] - {moedas[y]} - R${valorM[y]:.2f} {c}")
            y += 1

        print("[0] - Voltar")
        x = int(input("Selecione uma moeda:"))

        if x != 0 and x >= 1 and x <= len(moedas):
            x -= 1
            # mmoeda(x)

        elif x == 0:
            esperar()
        else:
            print("Opção inválida.\n")


minvest(saldo)
