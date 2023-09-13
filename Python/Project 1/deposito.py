saldo = 0

def sacar(saldo):
    while True:
        opcoes = ["200 R$", "500 R$", "1000 R$", "Outro Valor:"]
        for i, opcao in enumerate(opcoes):
            print(f"[{i + 1}] - {opcao}")
        print("[0] - Voltar\n")

        op = int(input("Digite o valor que deseja sacar:"))

        if op == 0:
            #os.system('cls')
            print("Voltando...\n")
            break
        
        if op == 4:
            op = float(input("Digite o valor que deseja sacar: "))

            if (saldo - op < 0):
                print("Saldo insuficiente")

            else:
                saldo -= op
                print(f"{op} R$ foi sacado, seu novo saldo é {saldo} R$\n")
        
        elif op <= len(opcoes):
            valor_saque = int(opcoes[op - 1].split()[0])

            if (saldo - valor_saque < 0):
                print("Saldo insuficiente")

            else:
                saldo -= valor_saque
                print(f"{valor_saque} R$ foi sacado, seu novo saldo é {saldo} R$\n")
        
        else:
            print("Opção Inválida\n")

sacar(saldo)