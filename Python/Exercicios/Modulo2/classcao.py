"""
Atividade: O cachorro modelo
➔ O QUE FAZER?
Em um arquivo .py, desenvolva uma página que “modela” um cachorro. Para isso, seu
algoritmo deve:
● Perguntar o nome e data de nascimento do cachorro ao ser acessada;
● Disponibilizar um botão com o texto “latir” que, ao ser clicado, exibe um alerta
com o texto “O cachorro latiu”;
● Disponibilizar um botão com o texto “comer” que, ao ser clicado, exibe um alerta
com o texto “O cachorro comeu”;
● Disponibilizar um botão com o texto “objeto cachorro” que, ao ser clicado, exibe
no console o objeto do cachorro.
"""


class Cao:
    def __init__(self, nome, nascimento):
        self.nome = str(nome)
        self.nascimento = str(nascimento)

    def latir(self):
        print(f"{self.nome} latiu")

    def comer(self):
        print(f"{self.nome} comeu")

    def objeto(self):
        print(f"Nome: {self.nome}, Data de Nascimento: {self.nascimento}")


def nomear():
    nome = input("Digite o nome do cachorro:")
    nascimento = input("Digite a data de nascimento:")
    cao1 = Cao(nome, nascimento)
    return cao1


cao1 = nomear()


# Menu
def menu():
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print("[1] - latir\n[2] - comer \n[3] - objeto\n[0] - Sair\n")

        x = int(input("Digite um numero:"))

        if x == 1:
            cao1.latir()
        elif x == 2:
            cao1.comer()
        elif x == 3:
            cao1.objeto()

        elif x == 0:
            print("Saindo...\n")
            break
        else:
            print("Opção Invalida")


menu()
