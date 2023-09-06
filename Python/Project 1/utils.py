#Menus

def menu1():
    while True:
        print("\n--------------------\n-----Menu A------\n--------------------\n")
        print("[1] - Opção 1\n[2] - Opção 2\n[0] - Voltar\n")
        op = int(input("Digite um numero:"))

        if op == 1:
            print("Opção 1 foi escolhida\n")
        elif op == 2:
            print("Opção 2 foi escolhida\n")
        elif op == 0:
            print("Voltando...\n")
            break
        else:
            print("Opção Invalida\n")

def menu2():
    while True:
        print("\n--------------------\n-----Menu B------\n--------------------\n")
        print("[1] - Opção 1\n[2] - Opção 2\n[0] - Voltar\n")
        op = int(input("Digite um numero:"))

        if op == 1:
            print("Opção 1 foi escolhida\n")
        elif op == 2:
            print("Opção 2 foi escolhida\n")
        elif op == 0:
            print("Voltando...\n")
            break
        else:
            print("Opção Invalida\n")

def mainMenu():
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print("[1] - Opção 1\n[2] - Opção 2\n[0] - Sair\n")

        op = int(input("Digite um numero:"))

        if op == 1:
            menu1()
        elif op == 2:
            menu2()
        elif op == 0:
            print("Saindo...\n")
            break
        else:
            print("Opção Invalida")

#Script
mainMenu()