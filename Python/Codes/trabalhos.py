#TV
def tv():
    p = int(input("Digite as polegadas:"))
    c = float(input("Digite o valor:"))

    if p < 32 and c > 1900:
        print("Não Comprar")
    elif p >= 32 and c <= 1900:
        print("Comprar")
    else:
        print("Não Comprar")

#Febre
def febre():       
    temp = float(input("Diga sua temperatura:"))

    if temp >= 38:
        print ("Está com febre.")
    elif temp >= 99:
        print ("Você não esta bem, sugiro ir em uma funeraria")
    else:
        print("Não está com febre")

#Frutas
def fruta():
    print("\n[1] - Tomate\n[2] - Laranja\n[3] - Abacaxi\n[4] - Limão")
    fruta = int(input("\nEscolha a fruta:"))

    if fruta == 1:
        valorAn = 3.99
        print("Tomate - R$",valorAn)
    elif fruta == 2:
        valorAn = 5.00
        print("Laranja - R$",valorAn)
    elif fruta == 3:
        valorAn = 6.50
        print("Abacaxi - R$",valorAn)
    elif fruta == 4:
        valorAn = 3.00
        print("Limão - R$",valorAn)
    else:
        print("\nEscolha uma fruta valida.")

    valorAt = float(input("\nInforme o valor atual:"))


    inflacao = valorAt - valorAn

    if inflacao > 0:
        print("\nInflacionou", round(inflacao, 2))
    elif inflacao == 0:
        print("\nNão inflacionou")
    else:
        print("\nNão inflacionou, diminuiu", inflacao)

#Menu de Seleção
def mainMenu():
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print("[1] - Tv\n[2] - Febre\n[3] - Fruta\n[0] - Sair\n")

        op = int(input("Digite um numero:"))

        if op == 1:
            tv()
        elif op == 2:
            febre()
        elif op == 3:
            fruta()
        elif op == 0:
            print("Saindo...\n")
            break
        else:
            print("Opção Invalida")


mainMenu()
