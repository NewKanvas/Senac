def menu():
    while True:
        title = "Menu"
        header = " " * 4 + f"{title}" + " " * 4
        overline = "_" * len(header)
        print(f"{overline}")
        overline = "‾" * len(header)
        print(header, f"\n{overline}")

        l = ["Cadastrar", "Evasão"]

        for i in range(len(l)):
            print(f"{i+1} - {l[i]}")

        x = input(">>")

        if x == 0:
            break
        if x ==


menu()