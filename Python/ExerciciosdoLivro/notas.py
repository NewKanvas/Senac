def check():
    n = int(input("Digite:"))

    if n >= 9:
        print("Excelente")

    elif n >= 8:
        print("Bom")

    elif n >= 5:
        print("Passou")

    elif n < 5:
        print("Reprovou")

#check()

def notas():
    n1 = 10
    n2 = 10
    n3 = 10
    
    me = (n1+n2+n3)/3
    ma = (n1+(n2*2)+(n3*3)+me)/7

    print(ma)

    if ma > 9:
        c = "A"
        r = "aprovado"
    
    elif ma > 7.5:
        c = "B"
        r = "aprovado"

    elif ma > 6:
        c = "C"
        r = "aprovado"
    
    elif ma > 4:
        c = "D"
        r = "reprovado"
    
    else:
        c = "E"
        r = "reprovado"

    print(f"O conceito do aluno é {c}\nEle foi {r}")


notas()