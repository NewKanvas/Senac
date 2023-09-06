#Functions
def MainMenu():
    print("*********************\n******Bem vindo******\n*********************\n")
    print("1.Opção 1\n2.Opção 2\n")
    op = (int(input("Digite um numero:")))

    return op

def SubMenu(op):
    if op == 1:
        return "Você escolheu a Opção 1"
    if op == 2:
        return "Você escolheu a Opção 2"
    else:
        return "Opção inválida"

#Script

MainMenu()
if op == 1:
    print("Você escolheu a Opção 1")
if op == 2:
    print("Você escolheu a Opção 2")
else:
    print("Opção inválida")