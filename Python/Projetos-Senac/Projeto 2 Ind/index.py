x = "eX_tX_pX_sX"
op = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"]
listY = []

print("**Menu inicial**")


for j in range(len(op)):
    underline = listC[1].find("_")
    e = listC[1][:underline]
    print(f"Avaliação de '{op[j]}': {e}")


def pedirNota():
    for i in range(len(op)):
        y = input(f'Digite o valor minimo da nota "{op[i]}"')
        listY.append(y)


# pedirNota()

"""
def veri():
    for j in range(len(op)):  # Dentro de um elemento só verifica o numero de letras

        letra = listC[0].find(op[j])

        underline = listC[0].find("_", j)
        # Como fazer para ele atualizar a posição do underline

        print(listC[0])
        print(f"{op[j]} = {listC[0][letra + 1 : underline]}")


veri()
"""
