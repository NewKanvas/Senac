def suporte():
    while True:
        print("--------------------\n-----Menu de Suporte------\n--------------------\n")
        print(
            "[1] - Como verificar seu saldo\n"
            "[2] - Como pagar sua fatura\n"
            "[3] - Como investir em moedas criptografadas\n"
            "[4] - Como solicitar um empréstimo\n"
            "[5] - Como fazer uma transferência\n"
            "[6] - Como verificar seu extrato\n"
            "[7] - Como esperar para atualizar os valores de moedas criptografadas\n"
            "[0] - Voltar\n"
        )

        x = int(input("Digite o número da opção que você deseja obter ajuda: "))

        if x == 0:
            print("Saindo do menu de suporte...")
            break
        elif x == 1:
            print("Para verificar seu saldo, selecione a opção 'Conta' no menu principal.")
        elif x == 2:
            print("Para pagar sua fatura, selecione a opção 'Conta' no menu principal e escolha 'Pagar Fatura'.")
        elif x == 3:
            print("Para investir em moedas criptografadas, selecione a opção 'Investimentos' no menu principal.")
        elif x == 4:
            print("Para solicitar um empréstimo, selecione a opção 'Empréstimo' no menu principal.")
        elif x == 5:
            print("Para fazer uma transferência, selecione a opção 'Transferência' no menu principal.")
        elif x == 6:
            print("Atualmente, a opção de verificação de extrato não está disponível.")
        elif x == 7:
            print("A opção 'Esperar' permite atualizar os valores de moedas criptografadas, mas o detalhe exato do processo não está especificado.")
        else:
            print("Opção inválida. Tente novamente.")

#suporte()

