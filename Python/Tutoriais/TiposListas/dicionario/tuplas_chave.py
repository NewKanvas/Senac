# usando tuplas como chaves de dicionários
# dicionário de telefones: chaves com nome e sobrenome
telefones = {
    ("Ana", "Santos"): "555-5550",
    ("Maria", "Nascimento"): "555-5551",
    ("Paula", "Melo"): "555-5552",
}

# iteerando sobre o dicionário
for nome, sobrenome in telefones:
    print(nome, sobrenome)

print("\n")
# ////////////////////////////////////////////////////////////#

# usando tuplas como chaves de dicionários
# dicionário de telefones: chaves com nome e sobrenome
telefones = {
    ("Ana", "Santos", "Marques"): "555-5550",
    ("Maria", "Nascimento", "Tele"): "555-5551",
    ("Paula", "Melo", "Castro"): "555-5552",
}

# iterando sobre o dicionário
for nome, sobrenome, teste in telefones:
    print(nome, sobrenome, teste)

print("\n")
# ////////////////////////////////////////////////////////////#

telefones = {
    ("Ana", "Santos", "Marques"): "555-5550",
    ("Maria", "Nascimento", "Tele"): "555-5551",
    ("Paula", "Melo", "Castro"): "555-5552",
}

for nome, telefone in telefones.items():
    nome_completo = " ".join(nome)
    print(f"Nome: {nome_completo}, Telefone: {telefone}\n")
