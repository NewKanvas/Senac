from artimetica import soma as add,subtracao as sub,multiplicacao as mult,divisao as div,mudarValor as cv

x =0
y = 0

while True:
    print("--------------------\n-----Calculadora------\n--------------------\n")
    print(f"X = {x}\nY = {y}\n")
    print(
            "[1] - Soma\n[2] - Subtração\n[3] - Multiplção\n[4] - Divisão\n[5] - Mudar valores\n[0] - Sair\n"
        )

    z = int(input("Digite o número da opção: "))

    if z == 0:
        print("Saindo ...")
        break

    elif z == 1:
        print(f"\nResultado da soma: {add(x, y)}")
    elif z == 2:
        print(f"\nResultado da subtração: {sub(x, y)}")
    elif z == 3:
        print(f"\nResultado da multiplicação: {mult(x, y)}")
    elif z == 4:
       print(f"\nResultado da divisão: {div(x, y)}")
    elif z == 5:
        x,y = cv(x,y)