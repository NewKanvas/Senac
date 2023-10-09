"""
Atividade: Implemente
➔ O QUE FAZER?
Crie um novo arquivo .py e implemente 3 novas funções conforme abaixo:
1. Uma função que acrescenta uma quantidade X de elementos a fila;
2. Uma função que verifica a quantidade de elementos na fila;
3. Uma função que verifica se a fila está vazia ou não.
"""


def acrescenta():
    x = int(input("Digite uma quantidades, para adcionar a fila:"))

    for i in range(0,x,1):
        lista1.append(i)

def quantidade():
    print(f"A lista possui {len(lista1)} elementos.")
    print(lista1)

def vazio():
    if len(lista1) == 0:
        print("Lista está vazia.")
    else:
        print("Listão não está vazia.")


lista1 = []


# Menu

while True:
    print("--------------------\n---Menu Principal---\n--------------------\n")
    opcoes = [
        "Adcionar",
        "Quantidade",
        "Está Vazia?"
    ]

    for i, opcao in enumerate(opcoes):
        print(f"[{i + 1}] - {opcao}")

    print("[0] - Sair\n")
    x = int(input("Digite um número:"))

    if x == 0:
        print("Saindo...\n")
        break

    if x == 1:
        acrescenta()
    elif x == 2:
        quantidade()
    elif x == 3:
        vazio()
    else:
        print("Opção Inválida\n")
        
    