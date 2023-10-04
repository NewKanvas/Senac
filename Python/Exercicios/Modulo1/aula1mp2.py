from time import sleep

# 1
def T1():
    x = 10 + 20 * 30 + 42 / 30 + (94 + 2) * 6 - 1
    

    print(x)

    sleep(2)
# 2
def T2():
    print((80*94)/10+55-90)
    print((10-7)/(67*5))
    print((12**4+5)*3+7)
    print(7%3**11*8-20-10/5*92)

    sleep(2)
#3
def T3():
    x = "Jonas"
    print(x)

    sleep(2)
#4
def T4():
    x = 10
    y = 2
    print(3*x-10*y)

    sleep(2)
#5
def T5():
    x = int(input("Digite o primeiro valor:"))
    y = int(input("Digite o segundo valor:"))

    z = ((x+y)/2)

    print(f"Sua media foi {z}")
    sleep(2)
#6
def T6():
    x = float(input("Digite o salario:"))
    z = x/30

    print(f"Seu salario é de {z} por dia.")
    sleep(2)
#7
def T7():
    x = input("Digite as 3 primeiras letras de um dia da semana(e.g. SEG):")

    if x == "SEG":
        print ("Segunda")
    if x == "TER":
        print ("Terça")
    if x == "QUA":
        print ("Quarta")
    if x == "QUI":
        print ("Quinta")
    if x == "SEX":
        print ("Sexta")
    if x == "SAB":
        print ("Sabado")
    if x == "DOM":
        print ("Domingo")  

    sleep(2)   

#8
def T8():
    a = 2
    b = 5.0
    c = 20
    d = 9
    f = 9

    print( 
    a==c,
    b>a,
    a<b,
    c>=f,
    d>b,
    f>=c,
    c!=f,
    c<=c,
    a==b,
    c<=f,
    c<d
    )
    
    sleep(2)

#9
def T9():
    a = False
    b = True
    c = True
    
    print(
        "a and (b or c)",a and (b or c),
        "\n(b and a) or c",(b and a) or c,
        "\nb and (not b)",b and (not b),
        "\nb or c",b or c,
        "\nnot c",not c,
        "\nc or a",c or a,
        "\nnot b",not b,
        "\nb or b",b or b,
        "\nnot a",not a,
        "\nc and c",c and c,
        "\na and b",a and b,
        "\nb or b",b or b,
        "\nb or c",b or c
    )

    sleep(2)

#10
def T10():
    A = 107
    B = 20
    C = False
    D = True
    print((A > B) and (C or D),"\n")
    A = 1
    B = 39
    C = False
    D = True
    print((A > B) and (C or D),"\n")
    A = 8
    B = 27
    C = True
    D = True
    print((A > B) and (C or D),"\n")

    sleep(2)

#11
def T11():
    x = float(input("Digite a distancia que deseja pecorrer em km:"))
    y = 10.97
    z = 13.90

    if x >= 300:
        print(z*x)

    else:
        print(y*x)
    
    sleep(2)

#12
def T12():
    x = int(input("Digite o primeiro valor:"))
    y = int(input("Digite o segundo valor:"))
    z = input("[1] -  Soma(+)\n[2] -  Subtração(-)\n[3] -  Divisão(/)\n[4] -  Multiplicação(*)\nDigite o simbolo ou numero correspondente:")

    if z == "+" or z == "1":
        print (x+y)
    if z == "-" or z == "2":
        print (x+y)
    if z == "/" or z == "3":
        print (x/y)
    if z == "*" or z == "4":
        print (x*y)

    else:
        print("Sinal invalido")

    sleep(2)

#13
def T13():
    x = int(input("Digite o valor(0 para sair):"))
    y = 0
    z = 0
    while x != 0:
        z = z+1
        y = y+x

        x = int(input("Digite o valor(0 para sair):"))

    print(f"{z} numeros foram digitados, a soma é {y}")


def mainMenu():
     menus = {
        1: T1,
        2: T2,
        3: T3,
        4: T4,
        5: T5,
        6: T6,
        7: T7,
        8: T8,
        9: T9,
        10: T10,
        11: T11,
        12: T12,
        13: T13

     }

     while True:
        print("--------------------\n---Menu de Seleção---\n--------------------\n")
        opcoes = ["#1", "#2", "#3", "#4","#5", "#6", "#7", "#8","#9", "#10", "#11", "#12","#13"]

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

mainMenu()