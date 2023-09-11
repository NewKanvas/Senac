def menuA():
    print("--------------------\n---Menu A---\n--------------------\n")
    op = int(input("Digite um numero:"))

def menuB():
    print("--------------------\n---Menu B---\n--------------------\n")
    op = int(input("Digite um numero:"))

def menuC():
    print("--------------------\n---Menu C---\n--------------------\n")
    op = int(input("Digite um numero:"))

def menuD():
    print("--------------------\n---Menu D---\n--------------------\n")
    op = int(input("Digite um numero:"))

def mainMenu():
     menus = {
         #objeto associando um numero a cada função
        1: menuA,
        2: menuB,
        3: menuC,
        4: menuD
     }

     while True:
        print("--------------------\n---Menu Principal---\n--------------------\n")
        opcoes = ["Menu A", "Menu B", "Menu C", "Menu D"]

        for i, opcao in enumerate(opcoes):
            print(f"[{i + 1}] - {opcao}")
            #enumerate da o índice a cada elemento da (opções)

        print("[0] - Sair\n")
        op = int(input("Digite um número:"))

        if op == 0:
            print("Saindo...\n")
            break

        if op in menus:
            print(f"{opcoes[op - 1]} foi escolhida\n")
            menus[op]()

        else:
            print("Opção Inválida\n")



mainMenu()