"""# Usuario exemplo:
contas = ["João", "Douglas"]
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 0]
fatura = [600, 600]
i = 0"""


def transf(valor, saldo, contas, conta1, conta2):
    saldo[conta1] = saldo[conta1] - valor
    print(f"{valor} foir retirado da sua conta, seu novo saldo é {saldo[conta1]}")

    # Esse usario nao deveria ver isso.
    saldo[conta2] = saldo[conta2] + valor
    print(
        f"{contas[conta1]} transferiu {valor} para sua conta, seu novo saldo é {saldo[conta2]}"
    )


def mtranf(contas, conta2, saldo, conta1):
    print(
        "--------------------\n-----Menu de Transferencia------\n--------------------\n"
    )
    print("[1] - 200 R$\n[2] - 500 R$ \n[3] - 1000 R$\n[0] - Voltar\n")
    print("Digite qualquer outro valor caso necessario.")

    valor = float(input("Digite o valor que deseja transferir (ou 0 para sair): "))

    if valor != 1 and valor != 2 and valor != 3 and valor != 0:
        transf(valor, saldo, contas, conta1, conta2)

    if valor == 1:
        transf(200, saldo, contas, conta1, conta2)
    if valor == 2:
        transf(500, saldo, contas, conta1, conta2)
    if valor == 3:
        transf(1000, saldo, contas, conta1, conta2)
    if valor == 0:
        pass


def mtranfsel(contas, saldo, i):
    while True:
        y = 0

        print(
            "--------------------\n-----Menu de Transferencia------\n--------------------\n"
        )
        print(f"Possiveis Transferencias:")

        for z in range(len(contas)):
            print(f"[{y+1}] - {contas[y]}")
            y += 1

        print("[0] - Voltar")
        x = int(input("Digite o usuario que voce deseja transferir:"))

        if x != 0 and x >= 1 and x <= len(contas):
            x -= 1
            mtranf(contas, x, saldo, i)

        elif x == 0:
            break
        else:
            print("Opção inválida.\n")


# mtranfsel()
