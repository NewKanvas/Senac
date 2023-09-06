#Menus

def menu1():
    print ("Hi")

def mainMenu():
    while True:
        print("--------------------\n-----Bem vindo------\n--------------------\n")
        print("[1] - Opção 1\n[2] - Opção 2\n[0] - Sair\n")

        op = int(input("Digite um numero:"))

        if op == 1:
            menu1()
        elif op == 2:
            pass
        elif op == 0:
            pass
            break
        else:
            print("Opção Invalida")

#Script
mainMenu()