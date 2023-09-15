from time import sleep

# 1
def T1():
    x = 10 +20*30
    y = 42/30 (94+2)* 6- 1

    print(x,y)

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
        a and (b or c),
        (b and a) or c,
        b and (not b),
        b or c,
        not c,
        c or a,
        not b,
        b or b,
        not a,
        c and c,
        a and b,
        b or b,
        b or c
    )

    sleep(2)

#10
def T10():
    pass

#11
def T11():
    pass

#12
def T12():
    pass

#13
def T13():
    pass



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