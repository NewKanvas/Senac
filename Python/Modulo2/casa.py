"""
Atividade: É de casa
➔ O QUE FAZER?
Criar três classes que representem as entidades Casa, Fatura e Pessoa; Com base
nelas, aplique os conceitos de agregação e composição;
Dica: lembrem que as pessoas que moram na casa pagam faturas. A partir destas
relações será possível aplicar os conceitos de agregação e combinação.
"""


class Casa:
    def __init__(self, endereço):
        self.endereço = endereço
        self.moradores = []

    def adcionarMorador(self, pessoa):
        self.moradores.append(pessoa)

    def mostrarMoradores(self):
        for i in self.moradores:
            print(i.nome, i.idade)


class Fatura:
    def __init__(self, valor):
        self.valor = float(valor)


class Pessoa:
    def __init__(self, nome, idade, endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço
        self.faturas = []
        endereço.adcionarMorador(self)

    def adicionarFatura(self, fatura):
        self.faturas.append(fatura)

    def mostrarDados(self):
        print(
            f"Nome: {self.nome}, Idade: {self.idade}, Morando em: {self.endereço.endereço}"
        )
        for fatura in self.faturas:
            print(fatura.valor)


casa1 = Casa("São Paulo")
pessoa1 = Pessoa("João", 21, casa1)


fatura1 = Fatura(200)
pessoa1.adicionarFatura(fatura1)


casa1.mostrarMoradores()

pessoa1.mostrarDados()


pessoa2 = Pessoa("Maria", 44, casa1)
fatura2 = Fatura(3000)
fatura3 = Fatura(250)

pessoa1.adicionarFatura(fatura3)
pessoa2.adicionarFatura(fatura2)

casa1.mostrarMoradores()
# pessoa1.mostrarDados()
# pessoa2.mostrarDados()
