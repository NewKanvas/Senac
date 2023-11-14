from time import sleep
import os
from cores import *
from matematica import *


def QnE():
    y = input("\n").lower()

    if y == "q":
        return -1
    elif y == "e":
        return 1
    elif y == "0":
        return "0"
    elif y == "":
        return 0


def tuto():
    os.system("cls")

    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)

    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")

    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


lista = {"Porcentagem": porcetangem, "Media": media, "Logaritimo": logaritimo}


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

        if y == 0:
            lista[list(lista.values())[x]]()

        x = x + y
        os.system("cls")


tuto()
menu()
