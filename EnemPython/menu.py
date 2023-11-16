from time import sleep
import os
from utils.biblioteca import *
from utils.cores import *
from materias.materias import *


def tuto():
    os.system("cls")

    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)

    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")

    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


# Tables


def porcentagem():
    title = "Porcentagem"
    texto = [
        "Porcentagem é uma forma de expressar uma parte de um todo em termos percentuais.",
        "Macete: Para calcular a porcentagem de um valor, multiplique o valor pela porcentagem e mova a vírgula duas posições para a frente. Por exemplo, 20 alunos representam 35%. 20 x 35 = 700. Portanto, 35% de 20 alunos são 7 alunas.",
        "Para encontrar a parte complementar (porcentagem restante), subtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres, então 100% - 35% = 65% são homens. Para calcular a quantidade, multiplique a porcentagem complementar pelo valor total e mova a vírgula duas posições para a frente. Assim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
    ]

    return title, texto


def matematica():
    title = "Matematica"
    lista = {
        "Porcentagem": porcentagem,
    }
    return title, lista


def materias():
    title = "Materias"
    lista = {
        "Matematica": matematica,
    }
    return title, lista


# end region


def menu2(title, lista):
    while True:
        os.system("cls")
        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)

        print(header, f"\n{overline}")

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        x = int(input("\n>> ")) - 1

        if x in range(len(lista)):
            os.system("cls")
            biblioteca(*lista[list(lista.keys())[x]]())

        else:
            print("Invalid Option")
        os.system("cls")


def menu(title, lista):
    while True:
        os.system("cls")
        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)

        print(header, f"\n{overline}")

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        x = int(input("\n>> ")) - 1

        if x in range(len(lista)):
            os.system("cls")
            menu2(*lista[list(lista.keys())[x]]())

        else:
            print("Invalid Option")
        os.system("cls")


# tuto()
menu(*materias())
