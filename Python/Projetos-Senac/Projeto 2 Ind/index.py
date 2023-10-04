x = "eX_tX_pX_sX"
op = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"]
listY = []

print("**Menu inicial**")


def pedirNota():
    for i in range(len(op)):
        y = input(f'Digite o valor minimo da nota "{op[i]}"')
        listY.append(y)


# pedirNota()


def veri():
    for i in listC:
        print(i)
        for j in range(len(op)):
            b = i.find(op[j])
            u = i.find("_")
            print(i[b + 1 : u])


veri()
