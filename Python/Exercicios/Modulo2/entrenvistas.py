"""
Atividade: Organizando as entrevistas
➔ O QUE FAZER?
Em um arquivo .py, desenvolva uma classe com os seguintes requisitos:
1. Tenha os atributos: idade, cidade, estado, salário atual e escolaridade
2. Tenha um método imprimirDados que devolva as informações do entrevistado
em uma string com os atributos separados por vírgula (Ex: 20,Rio de
Janeiro,RJ,1000,Ensino Médio Completo
"""


# Má pratica
print("Má pratica")


class Char:
    def __init__(self):
        self.idade = ""
        self.cidade = ""
        self.estado = ""
        self.salario = ""
        self.escolaridade = ""

        self.idade = input("Digite sua idade:")
        self.cidade = input("Digite sua cidade:")
        self.estado = input("Digite seu estado:")
        self.salario = input("Digite seu salario atual:")
        self.escolaridade = input("Digite sua escolaridade:")

    def imprimirDados(self):
        print(
            f"\n\nIdade: {self.idade};\nCidade: {self.cidade};\nEstado: {self.estado};\nSalario: {self.salario};\nEscolaridade: {self.escolaridade};\n"
        )


char1 = Char()
char1.imprimirDados()


######
# Boa pratica
print("Boa pratica")


class Dar:
    def __init__(self, idade, cidade, estado, salario, escolaridade):
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.salario = salario
        self.escolaridade = escolaridade

    def imprimirDados(self):
        print(
            f"\n\nIdade: {self.idade};\nCidade: {self.cidade};\nEstado: {self.estado};\nSalario: {self.salario};\nEscolaridade: {self.escolaridade}.\n"
        )


def iniciar():
    idade = input("Digite sua idade:")
    cidade = input("Digite sua cidade:")
    estado = input("Digite seu estado:")
    salario = input("Digite seu salario atual:")
    escolaridade = input("Digite sua escolaridade:")
    c = Dar(idade, cidade, estado, salario, escolaridade)
    return c


pessoa = iniciar()
pessoa.imprimirDados()
