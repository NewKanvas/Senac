"""
Atividade: Tudo na cápsula
➔ O QUE FAZER?
1. Criar uma classe Pessoa com os atributos nome e CPF como privados;
2. Criar os métodos para acessar e alterar o valor desses atributos com o intuito
de reproduzir o conceito de encapsulamento;
3. Realizar uma demonstração do funcionamento do que foi implementado.
"""


class Pessoa:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nNome):
        self._nome = nNome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, nCpf):
        self._nome = nCpf


p1 = Pessoa("Jonas", 20202020)
print(p1.get_nome())
p1.set_nome("João")
print(p1.get_nome())
