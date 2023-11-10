from time import sleep
import os


x = "eX_tX_pX_sX" #Modelo
op = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"] #Strings recebidas
listY = [] #Lista de dicionarios



def filtrar():
    os.system("cls")
    print("**Filtrando**")
    sleep(2)

    # Divide
    for j in range(len(listC)):
        nLista = listC[j].split("_")

        listYD = {}

        # Inclui como dicionario

        for i in range(len(nLista)):
            valor = int(nLista[i][1:])
            listYD[op[i]] = valor
        listY.append(listYD)

    listC.clear()  # Apaga lista ja filtrada


def pedirNota():
    listX = {} #Lista e notas minimas
    
    # pedir nota
    os.system("cls")
    for i in range(len(op)):
        y = int(input(f'Digite o valor minimo da nota "{op[i]}":'))
        listX[op[i]] = y

    print("\n")

    # Verificação
    for i in range(len(listY)):
        status = 0

        for j in range(len(op)):
            if listY[i][op[j]] >= listX[op[j]]:
                status = status + 1
        if status == 4:
            print(f"Candidato {i + 1} foi aprovado.")

    print("\nSe nada for informado, nenhum candidato foi aprovado")
    sleep(2)


def info():
    os.system("cls")
    for i in range(len(listY)):
        print(f"Candidato {i + 1}:\n")
        print(
            f"Entrevista: {listY[i]['e']};\nTeste teórico: {listY[i]['t']};\nTeste prático: {listY[i]['p']};\nSoft skills: {listY[i]['s']}\n"
        )
    sleep(2)


def add():
    os.system("cls")
    n = {}

    for i in range(len(op)):
        valor = input(f'Digite o valor da nota "{op[i]}": ')
        n[op[i]] = valor

    listY.append(n)

    print("Novo candidato adicionado!")
    sleep(2)


def rem():
    while True:
        os.system("cls")
        for i in range(len(listY)):
            print(f"Candidato {i + 1}:")
            print(
                f"Entrevista: {listY[i]['e']};\nTeste teórico: {listY[i]['t']};\nTeste prático: {listY[i]['p']};\nSoft skills: {listY[i]['s']}\n"
            )

        print("Digite [0] para sair")
        x = int(input("Digite o numero do candidato para removelo:"))

        if x == 0:
            print("Saindo...")
            sleep(2)
            break
        elif x > 0:
            print(f"Candidato {x} foi removido.")
            listY.pop(x - 1)
            sleep(2)
            break
        else:
            print("Opção Inválida\n")
            sleep(2)


# Menu
filtrar()


while True:
    print("--------------------\n---Menu Principal---\n--------------------\n")
    opcoes = [
        "Filtrar",
        "Buscar Candidatos",
        "Adcionar Candidato",
        "Remover Candidato",
        "Info",
    ]

    for i, opcao in enumerate(opcoes):
        print(f"[{i + 1}] - {opcao}")
        # enumerate da o índice a cada elemento da (opções)

    print("[0] - Sair\n")
    x = int(input("Digite um número:"))

    if x == 0:
        print("Saindo...\n")
        break

    if x == 1:
        filtrar()
    elif x == 2:
        pedirNota()
    elif x == 3:
        add()
    elif x == 4:
        rem()
    elif x == 5:
        info()

    else:
        print("Opção Inválida\n")
