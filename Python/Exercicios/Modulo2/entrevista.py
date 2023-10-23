"""
Atividade: Quem foi entrevistado?
➔ O QUE FAZER?
No mesmo arquivo .py, desenvolva uma classe Pesquisa com os seguintes requisitos:
1. Tenha os atributos: nome e listaEntrevistados
2. Tenha um método imprimirEntrevistados que vai chamar a função imprimirDados
de cada um dos entrevistados que forem adicionados a uma pesquisa criada.
"""


class Entrevistado:
    def __init__(self, nome, idade, cidade, estado, salario, escolaridade):
        self.nome = str(nome)
        self.idade = str(idade)
        self.cidade = str(cidade)
        self.estado = str(estado)
        self.salario = float(salario)
        self.escolaridade = str(escolaridade)

    def imprimirDados(self):
        print(
            f"\nNome: {self.nome}\nIdade: {self.idade};\nCidade: {self.cidade};\nEstado: {self.estado};\nSalario: {self.salario};\nEscolaridade: {self.escolaridade};\n"
        )


####


def imprimirEntrevistados():
    for i in listaEntrevistados:
        i.imprimirDados()


####

listaEntrevistados = []


def iniciar():
    nome = input("Digite sua nome:")
    idade = input("Digite sua idade:")
    cidade = input("Digite sua cidade:")
    estado = input("Digite seu estado:")
    salario = input("Digite seu salario atual:")
    escolaridade = input("Digite sua escolaridade:")
    entrevistados = Entrevistado(nome, idade, cidade, estado, salario, escolaridade)
    listaEntrevistados.append(entrevistados)

    return entrevistados


pessoa = Entrevistado("J", 1, 1, 1, 1, 1)
listaEntrevistados.append(pessoa)

pessoa2 = Entrevistado("K", 2, 2, 2, 2, 2)
listaEntrevistados.append(pessoa2)

imprimirEntrevistados()
