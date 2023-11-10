"""
O que é para fazer:

Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. Em seguida, crie um objeto da classe Aluno, leia os valores de nome, idade e matrícula desse objeto do usuário e exiba na tela os dados do aluno cadastrado.

Como Fazer:

    Crie uma classe chamada Aluno;
    Defina os atributos nome, idade e matrícula da classe Aluno;
    Crie um objeto da classe Aluno;
    Peça ao usuário para digitar os valores de nome, idade e matrícula do objeto;
    Exiba na tela os dados do aluno cadastrado.
"""


class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def dados(self):
        print(self.nome, self.idade, self.matricula)


def iniciar():
    nome = input("Digite nome:")
    idade = input("Digite idade:")
    matricula = input("Digite matricula:")
    a = Aluno(nome, idade, matricula)
    return a


aluno1 = iniciar()
aluno1.dados()
