"""Atividade: Enquete
➔ O QUE FAZER?
Crie o algoritmo abaixo:

1. Crie uma lista de pessoas que devam participar de
uma enquete sobre sua linguagem favorita.

2. Monte um dicionário com as pessoas que
responderam ou não a essa enquete.

3. Percorra a lista de pessoas que devem participar
da enquete. Se elas já tiverem respondido à
enquete, mostre uma mensagem
agradecendo-lhes por responder. Se ainda não
participaram da enquete, apresente uma
mensagem convidando-as a responder."""


pd = {"João": "Java", "Maria": "Python", "Fulano": ""}


for i, (nome, linguagem) in enumerate(pd.items()):
    # pd.items retorna duplas em tuplas; e.g("João", "Java").
    # O enumerate percorre essas listas e numera elas.
    if not linguagem:
        print(f"{nome} não respondeu.")
        x = input(f"Deseja responder, {nome}? [Y/N]: ").lower()
        if x == "y":
            y = input(f"Digite a linguagem de {nome}: ")
            pd[nome] = y
            print(pd)


