"""contas = ["João", "Douglas"]
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 0]
fatura = [600, 600]
i = 0"""


def empre(valor, saldo, i, fatura, renda):
    if valor > renda[i] * 2:
        print("Valor negado. O valor solicitado excede o dobro da renda.")
    else:
        print("Valor aceito.")
        saldo[i] += valor
        juros = (valor * (20 / 100)) + valor
        print(
            f"Seu empréstimo de {valor}R$ foi adicionado à sua conta.\nSeu saldo é de {saldo[i]}.\nVocê terá que pagar {juros}R$"
        )

        fatura[i] = juros
        # Atualizar o valor da fatura


def menuEmp(saldo, i, fatura, renda):
    while True:
        print(
            "--------------------\n-----Menu de Empréstimo------\n--------------------\n"
        )
        print("[1] - 200 R$\n[2] - 500 R$ \n[3] - 1000 R$\n[0] - Voltar\n")
        print("Digite qualquer outro valor caso necessario.")
        x = float(input("Digite o valor desejado (ou 0 para sair): "))

        if x == 0:
            print("Saindo...")
            break

        if x != 1 and x != 2 and x != 3 and x != 0:
            empre(x, saldo, i, fatura, renda)

        if x == 1:
            empre(200, saldo, i, fatura, renda)
        if x == 2:
            empre(500, saldo, i, fatura, renda)
        if x == 3:
            empre(1000, saldo, i, fatura, renda)


# menuEmp(saldo, renda, i)
