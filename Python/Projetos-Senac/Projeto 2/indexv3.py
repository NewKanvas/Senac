from time import sleep
import os
from quiz import *
from cores import *


# iniciar Classe
def iniciar():
    while True:
        respostas = {}

        idade(respostas)
        genero(respostas)
        estado(respostas)
        perguntas(respostas)
        p = Candidato(
            respostas["Idade"],
            respostas["Genero"],
            respostas["Estado"],
            respostas["R1"],
            respostas["R2"],
            respostas["R3"],
            respostas["R4"],
        )
        p.salvar()


# Mensagem de Apresentação
def apresentacao():
    print("**Pesquisa sobre Diversidade no Local de Trabalho**\n")
    sleep(3)
    os.system("cls")

    print("Bem-vindo à nossa pesquisa sobre diversidade no local de trabalho!")
    sleep(2)

    print(
        "Estamos empenhados em promover um ambiente de trabalho inclusivo e igualitário para todos os nossos colaboradores."
    )
    sleep(4)

    print(
        "Esta pesquisa tem como objetivo coletar opiniões e percepções sobre a diversidade e inclusão em nossa organização."
    )
    sleep(4)

    print(
        "Suas respostas são extremamente valiosas e nos ajudarão a tomar medidas para melhorar nossa cultura empresarial.\n"
    )
    sleep(4)


# apresentacao()
iniciar()
