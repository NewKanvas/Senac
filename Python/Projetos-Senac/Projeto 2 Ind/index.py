x = "eX_tX_pX_sX"
op = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"]
listY = []
listX = {}

def filtrar():
    print("**Filtrando**")

    for j in range(len(listC)):
        nLista = listC[j].split("_")
        #print(nLista)

        listYD = {}

        for i in range(len(nLista)):
            valor = int(nLista[i][1:])
            listYD[op[i]] = valor
        listY.append(listYD)
        
    
    print(listY)
    print(len(listY))
    print(listC)


def pedirNota():
    for i in range(len(op)):
        y = int(input(f'Digite o valor minimo da nota "{op[i]}":'))
        listX[op[i]] = y
    #print(listX)

    print("\n")
        
    #Verificação
    for i in range(len(listY)):
        status = 0

        for j in range(len(op)):
            if listY[i][op[j]] >= listX[op[j]]:
                status = status+1
        if status == 4:
            print (f"Candidato {i + 1} foi aprovado.")


def info():
    for i in range(len(listY)):
        print(f"Candidato {i + 1}:\n")
        print(f"Entrevista: {listY[i]['e']};\nTeste teórico: {listY[i]['t']};\nTeste prático: {listY[i]['p']};\nSoft skills: {listY[i]['s']}")


def add():
    pass

#Menu
filtrar()


while True:
    print("--------------------\n---Menu Principal---\n--------------------\n")
    opcoes = ["Filtrar", "Nota Minina", "Adcionar", "Info"]

    for i, opcao in enumerate(opcoes):
        print(f"[{i + 1}] - {opcao}")
        #enumerate da o índice a cada elemento da (opções)

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
        info()

    else:
        print("Opção Inválida\n")

