from time import sleep
import os
from cores import *
from matematica import *
import msvcrt


def QnE():
    if msvcrt.kbhit():
        y = msvcrt.getch().decode().upper()
        print(y)
        return y  # Return the key value
    else:
        return ""  # Return an empty string if no key is pressed


def tuto():
    os.system("cls")

    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)

    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")

    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


lista = {
    "Porcentagem": porcentagem,
    "Media": media,
    "Logaritimo": logaritimo,
    "Geometria": geometria,
    "Equações Lineares": equacoes_lineares,
    "Trigonometria": trigonometria,
}


def menu():
    x = 0

    while True:
        if x < 0:
            x = len(lista) - 1
        elif x >= len(lista):
            x = 0

        print("** Matematica **\n")
        for i, op in enumerate(lista):
            if x == i:
                print(f">> [{i+1}] {op}")
            else:
                print(f"[{i+1}] {op}")
        y = QnE()

        if y == "":
            pass  # Do nothing if no key is pressed
        else:
            lista[list(lista.keys())[x]]()

        x = x + y
        os.system("cls")


tuto()
menu()
