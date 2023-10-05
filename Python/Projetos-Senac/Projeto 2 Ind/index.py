x = "eX_tX_pX_sX"
op = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"]
listY = []
listX = {}

print("**Filtragem**")

for j in range(len(listC)):
    nLista = listC[j].split("_")
    #print(nLista)

    listYD = {}

    for i in range(len(nLista)):
        valor = int(nLista[i][1:])
        listYD[op[i]] = valor
    listY.append(listYD)
    
'''print(listY)
print(len(listY))'''


def pedirNota():
    for i in range(len(op)):
        y = int(input(f'Digite o valor minimo da nota "{op[i]}"'))
        listX[op[i]] = y
    print(listX)
        
    for i in range(len(listY)):
        for j in range(len(op)):
            '''elemento = listY[i][op[j]]
            print(f"Elemento relacionado à letra '{op[j]}' no dicionário {i} da lista: {elemento}")'''

            if listY[i][op[j]] < listX[op[j]]:
                print(f"Candidato {i + 1} é menor em '{op[j]}'")
            elif listY[i][op[j]] > listX[op[j]]:
                print(f"Candidato {i + 1} é maior em '{op[j]}'")

pedirNota()

