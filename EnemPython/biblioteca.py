def porcentagem():
    title = "Porcentagem"
    texto = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
    ]
    return title, texto


def QnE():
    x = input(" >> ").upper()
    if x == "Q":
        return -1
    elif x == "E":
        return 1
    elif x == "0":
        return 2


def biblioteca(title, texto):
    op = 0

    while True:
        if op < 0:
            op = len(texto) - 1
        elif op >= len(texto):
            op = 0

        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)
        print(header, f"\n{overline}")

        print(texto[op], "\n")

        if op == 0:
            print(f"{len(texto)}<<{op+1}>>{op+2}")

        elif op == len(texto) - 1:
            print(f"{op}<<{op+1}>>{1}")

        else:
            print(f"{op}<<{op+1}>>{op+2}")

        x = QnE()

        if x == 2:
            break

        op = op + x


biblioteca(*porcentagem())
