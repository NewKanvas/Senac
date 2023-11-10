saldo = 3000

def emprestimo():
    # Tem quer ter essa informação previa
    saldo = 3000
    renda = 1320

    while True:
        # Fazer menu, esse codigo e apenas a logica.

        emp = float(input("Digite o valor desejado (ou 0 para sair): "))

        if emp == 0:
            print("Saindo...")
            break

        if emp > renda * 2:
            print("Valor negado. O valor solicitado excede o dobro da renda.")
        else:
            print("Valor aceito.")
            saldo += emp
            juros = (emp * (20 / 100)) + emp
            print(
                f"Seu emprestimo de {emp}R$ foi adcionado a sua conta.\nSeu saldo é de {saldo}.\nVocê tera que pagar {juros}R$"
            )

def deposito():
    while True:
        #os.system('cls')
        print("Menu de deposito\n(Todos os depositos sao via PIX)")
        opcoes = ["80 R$", "100 R$", "500 R$","1000 R$", "Outro Valor:"]
        for i, opcao in enumerate(opcoes):
            print(f"[{i + 1}] - {opcao}")
        print("[0] - Voltar\n")

        op = int(input("Escolha uma opção:"))

        if op == 0:
            #os.system('cls')
            print("Voltando...\n")
            break
        
        if op == 4:
            op = float(input("Digite o valor que deseja depositar: "))
            print(f"{op} R$ sera depositado, aguardando pagamento.\n")
            print(f"CODIGO FICCIONAL\n")
        
        elif op <= len(opcoes):
            valor_saque = int(opcoes[op - 1].split()[0])
            print(f"{valor_saque} R$ sera depositado, aguardando pagamento.\n")
            print(f"CODIGO FICCIONAL\n")

        else:
            print("Opção Inválida\n")

deposito()