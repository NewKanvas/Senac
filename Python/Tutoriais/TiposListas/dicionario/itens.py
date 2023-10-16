#lista de tuplas
#definindo
lista_tuplas = [(0,1), (1,2),(2,3),(3,4)]

#verificando os tipos de cada item
print(type(lista_tuplas))
print(type(lista_tuplas[0]))

#////////////////////////////////////////////////////////////#

#usando a função zip
lista01 = [1,2,3,4,5]
lista02 = ['a','b','c','d','e']

print(zip(lista01,lista02))
#Iterando sobre zip
for item1, item2 in zip(lista01,lista02):
    print(f'item 1:{item1} e item 2:{item2}')

#////////////////////////////////////////////////////////////#

#usando a função zip
lista01 = [1,2,3,4,5]
lista02 = ['a','b','c','d','e']
lista03 = [1,2,3,4,5]

print(zip(lista01,lista02))
#Iterando sobre zip
for item1, item2, item3 in zip(lista01,lista02,lista03):
    print(f'item: {item3} : {item1} :{item2} ')

#////////////////////////////////////////////////////////////#

#lista de dicionários
carro01 = {'cor': 'preto', 'motor': 2.0, 'ano':2012}
carro02 = {'cor': 'branco', 'motor': 1.0, 'ano':2013}
carro03 = {'cor': 'prata', 'motor': 2.4, 'ano':2014}
carro04 = {'cor': 'vermelho', 'motor': 1.6, 'ano':2015}

lista_carros = [carro01, carro02, carro03, carro04]

#iterando sobre a lista de carros
for carro in lista_carros:
    print(carro)

#////////////////////////////////////////////////////////////#

#lista de dicionários
carro01 = {'cor': 'preto', 'motor': 2.0, 'ano':2012}
carro02 = {'cor': 'branco', 'motor': 1.0, 'ano':2013}
carro03 = {'cor': 'prata', 'motor': 2.4, 'ano':2014}
carro04 = {'cor': 'vermelho', 'motor': 1.6, 'ano':2015}


#declarando dicionário de dicionários
dic_carros = {
    'Gol': carro01,
    'Corsa': carro02,
    'Hilux': carro03,
    'Fiesta': carro04
}
#iterando sobre dicionário de dicionários
for key in dic_carros:
    print(dic_carros[key])

#////////////////////////////////////////////////////////////#

#usando tuplas como chaves de dicionários
#dicionário de telefones: chaves com nome e sobrenome
telefones = {
    ('Ana', 'Santos'): '555-5550',
    ('Maria', 'Nascimento'): '555-5551',
    ('Paula', 'Melo'): '555-5552',
}

#iteerando sobre o dicionário
for nome,sobrenome in telefones:
    print(nome,sobrenome)

#////////////////////////////////////////////////////////////#

#usando tuplas como chaves de dicionários
#dicionário de telefones: chaves com nome e sobrenome
telefones = {
    ('Ana', 'Santos', 'Marques'): '555-5550',
    ('Maria', 'Nascimento', 'Tele'): '555-5551',
    ('Paula', 'Melo', 'Castro'): '555-5552',
}

#iterando sobre o dicionário
for nome,sobrenome,teste in telefones:
    print(nome,sobrenome,teste)

#////////////////////////////////////////////////////////////#

telefones = {
    ('Ana', 'Santos', 'Marques'): '555-5550',
    ('Maria', 'Nascimento', 'Tele'): '555-5551',
    ('Paula', 'Melo', 'Castro'): '555-5552',
}

for nome, telefone in telefones.items():
    nome_completo = ' '.join(nome)
    print(f"Nome: {nome_completo}, Telefone: {telefone}\n")