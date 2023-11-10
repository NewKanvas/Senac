"""
Atividade: Computador de bordo
➔ O QUE FAZER?
Desenvolva uma página que “emula” um computador de bordo de automóvel. Para isso::
1. Seu algoritmo deve possuir um objeto que represente um carro com as características:
cor, capacidade do tanque, quantidade de combustível no tanque, consumo médio
(Km/Litro);
2. O carro deve possuir métodos que:
a. Forneçam a previsão de quantos KM espera-se rodar com a quantidade de combustível e o
consumo médio;
b. Ande uma determinada quantidade de Km (argumento) e diminua a quantidade de gasolina
do tanque a partir da quantidade Km rodados e a média de consumo;
c. Getters e Setters para: cor, capacidade do tanque e consumo médio;
d. Construtor com modelo e cor.
"""


class Carro:
    def __init__(self, cor, cap_tanque, qtd_combustivel, c_medio):
        self.cor = str(cor)
        self.cap_tanque = float(cap_tanque)
        self.qtd_combustivel = float(qtd_combustivel)
        self.c_medio = c_medio

    # A

    def prev(self):
        m = self.qtd_combustivel / self.c_medio
        print(
            f"Com {self.qtd_combustivel} no tanque, espera-se rodar aproximadamente {m:.0f}Km"
        )

    # B

    def andar(self):
        m = float(input("Digite a quantidade de Km a serem andados:"))

        total = m * self.c_medio

        if total <= self.qtd_combustivel:
            self.qtd_combustivel = self.qtd_combustivel - total
            print(
                f"Você percorreu {m:.0f} km. Restam {self.qtd_combustivel:.2f} litros de combustível no tanque."
            )
        else:
            print("Você não tem combustível suficiente para isso.")

    # C

    def set_cor(self, Ncor):
        self.cor = Ncor

    def set_cap_tanque(self, Ncap_tanque):
        self.cap_tanque = Ncap_tanque

    def set_qtd_combustivel(self, Nqtd_combustivel):
        self.qtd_combustivel = Nqtd_combustivel

    def set_c_medio(self, Nc_medio):
        self.c_medio = Nc_medio

    # C.2

    def get_cor(self):
        return self.cor

    def set_cap_tanque(self):
        return self.cap_tanque

    def set_qtd_combustivel(self):
        return self.qtd_combustivel

    def set_c_medio(self):
        return self.c_medio

    # D

    # Construtor com modelo e cor?


"""c = Carro("Amarelo", 100, 100, 2)
c.prev()
c.andar()"""


# Menu
def iniciar():
    while True:
        print("Crie um carro.")
        cor = input("Digite a cor do carro")
        cap_tanque = float(input("Digite a capacidade maxima do tanque do carro"))
        qtd_combustivel = float(input("Digite a quantidade de combustivel do carro"))
        c_medio = float(input("Digite a do carro"))
        carro = Carro(cor, cap_tanque, qtd_combustivel, c_medio)
        break


def menuset():
    while True:
        print("Menu da Set do Carro")
        op = ["cor", "cap_tanque", "qtd_combustivel", "c_medio"]

        for i in range(len(op)):
            print(f"[{i}] - {op[i]}")

        x = int(input("Digite o numero correspondente a sua resposta:"))


def menu():
    while True:
        print("Menu da Classe Carro")
        op = [
            "Andar",
            "Set",
            "Get",
        ]

        for i in range(len(op)):
            print(f"[{i}] - {op[i]}")

        x = int(input("Digite o numero correspondente a sua resposta:"))

        if x == 2:
            menuset()


iniciar()
menu()
