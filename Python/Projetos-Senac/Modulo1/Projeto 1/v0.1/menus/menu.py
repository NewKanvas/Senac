import os

def menuA():
    #submenus = {}

    while True:
        print("--------------------\n---Menu A---\n--------------------\n")

        opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

        for i, opcao in enumerate(opcoes):
            print(f"[{i + 1}] - {opcao}")

        print("[0] - Voltar\n")
        op = int(input("Digite um numero:"))

        if op == 0:
            os.system('cls')
            print("Saindo...\n")
            break

        elif op > 0:
            os.system('cls')
            print(f"{opcoes[op - 1]} foi escolhida\n")

        #if op in menus:
            #print(f"{opcoes[op - 1]} foi escolhida\n")
            #menus[op]()

        else:
            print("Opção Inválida\n")

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
            os.system('cls')
            print("Saindo...\n")
            break

        if op in menus:
            os.system('cls')
            print(f"{opcoes[op - 1]} foi escolhida\n")
            menus[op]()

        else:
            print("Opção Inválida\n")



mainMenu()