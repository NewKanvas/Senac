from artimetica import soma,subtracao,multiplicacao,divisao,mudarValor

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
        print(f"\nResultado da soma: {soma(x, y)}")
    elif z == 2:
        print(f"\nResultado da subtração: {subtracao(x, y)}")
    elif z == 3:
        print(f"\nResultado da multiplicação: {multiplicacao(x, y)}")
    elif z == 4:
       print(f"\nResultado da divisão: {divisao(x, y)}")
    elif z == 5:
        x,y = mudarValor(x,y)