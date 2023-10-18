# Exemplo 1
# Definindo uma classe chamada "Pessoa"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")


# Criando dois objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Chamando o método saudacao para cada objeto
pessoa1.saudacao()  # Saída: "Olá, meu nome é Alice e eu tenho 30 anos."
pessoa2.saudacao()  # Saída: "Olá, meu nome é Bob e eu tenho 25 anos."

# Exemplo 2


# Definindo uma classe chamada "Cliente"
class Cliente:
    # Nela vai ter esses parametros.
    # __init__ "inicializar os atributos de um objeto"
    # self significa que voce vai dar o valor dos parametros.

    def __init__(self, nome, telefone, numero, saldo, limite):
        self.nome = str(nome)  # Recebendo Nome em Str
        self.telefone = str(telefone)  # Recebendo Telefone em Str
        self.numero = str(numero)  # Recebendo Numero em Str
        self.saldo = saldo  # Recebendo Saldo
        self.limite = limite  # Recebendo Limite
        # inicia extrato
        self.extrato = []  # Nao tem valor inicial

    def mostraCliente(self):
        print(
            f"Nome: {self.nome}, telefone: {self.telefone}, Numero: {self.numero}, Saldo: {self.saldo}, limite: {self.limite}"
        )


teste = Cliente("Ana", "90999-0000", 10029, 100.45, 3000.00)

teste.mostraCliente()
