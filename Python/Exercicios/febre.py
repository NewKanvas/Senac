while True:
    #Termometro
    def term(x):
        if x >= 38 and x <= 39:
            print("\nVocê está com febre. Tome um remédio e repouse.\n")

        elif x > 39:
            print("\nVocê está com febre. Tome um remédio,procure um médico.\n")

        else:
            print("\nNada de febre.\n")

    #Funcionando

    x = input("\nDigite um número, ou 'sair' para sair: ")

    if x == ("sair"):
        print("Saindo...")
        break

    else:
        x = int(x)
        term(x)

