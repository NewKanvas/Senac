"""# Usuario exemplo:
cntas = ["João", "Douglas"]
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 0]
fatura = [600, 600]o
i = 0"""


def esperar(valorM, sorte, v):
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


def extrato():
    print("Extrato da conta:")
    # Incluir detalhes do extrato, como transações, datas, etc.
    print("Extrato não disponível no momento.")


def pagarf(saldo, fatura, i):
    print(f"Sua fatura é de {fatura[i]}\nTem certeza que deseja pagar a fatura?")

    x = input('Digite[Y] para "Sim" ou [N] para "Não":').lower()

    if x == "y":
        if saldo[i] >= fatura[i]:
            saldo[i] -= fatura[i]
            print(
                f"Fatura de R${fatura[i]}, foi paga com sucesso.\nSeu novo saldo é de R${saldo[i]}."
            )

            fatura[i] = 0

        else:
            print("Saldo insuficiente para pagar a fatura.")

    elif x == "n":
        print("Pagamento da fatura cancelado.")

    else:
        print("Opção inválida.")


def conta(saldo, i, fatura, valorM, sorte, v):
    while True:
        print("--------------------\n-----Menu Conta------\n--------------------\n")
        print(
            "[1] - Saldo\n[2] - Extrato \n[3] - Pagar Fatura\n[4] - Esperar\n[0] - Voltar\n"
        )

        x = int(input("Digite um numero:"))

        if x == 0:
            print("Saindo...")
            break

        if x == 1:
            print(f"Seu saldo é de R${saldo[i]}")

        if x == 2:
            extrato()

        if x == 3:
            print(f"[Pagar Fatura] Selecionado")
            pagarf(saldo, fatura, i)

        if x == 4:
            print("Esperando...")
            esperar(valorM, sorte, v)


# conta(saldo, i)
