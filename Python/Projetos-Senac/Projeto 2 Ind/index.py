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
        #Sera preciso apagar a listaC apos a filtragem caso fosse algo real.
    
    '''print(listY)
    print(len(listY))'''


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


'''menus = {
         #objeto associando um numero a cada função
        1: filtrar,
        2: pedirNota,
        3: add,
        4: info

     }'''

'''while True:
    print("--------------------\n---Menu Principal---\n--------------------\n")
    opcoes = ["Filtrar", "Nota Minina", "Adcionar", "Info"]

    for i, opcao in enumerate(opcoes):
        print(f"[{i + 1}] - {opcao}")
        #enumerate da o índice a cada elemento da (opções)

    print("[0] - Sair\n")
    op = int(input("Digite um número:"))

    if op == 0:
        print("Saindo...\n")
        break

    if op in menus:
            print(f"{opcoes[op - 1]} foi escolhida\n")
            menus[op]()

    else:
        print("Opção Inválida\n")

'''
