import csv

# import pandas as pd
from time import sleep
import os


def coletar_info():
    listaC = []

    while True:
        respostas = {}  # Dicionario para as respostas.

        os.system("cls")

        # Pergunta de Genero

        print("Identifique seu gênero.")
        print("[1] - Masculino [2] - Feminino [3] - Não Binário")
        genero = int(input("Digite o número correspondente ao seu gênero: "))

        # Transformação da respotas de Genero

        if genero == 1:
            respostas["Genero"] = "M"
        elif genero == 2:
            respostas["Genero"] = "F"
        elif genero == 3:
            respostas["Genero"] = "NB"

        else:
            print("Opção inválida. Tente novamente.")
            sleep(1)
            continue

        # Pergunta da Idade
        while True:
            os.system("cls")

            idade = input("Identifique sua idade (ou '00' para sair): ")

            if idade == "00":  # Sai de dentro do loop
                break

            idade = int(idade)

            if idade > 0:
                respostas["Idade"] = idade
                break

            else:
                print("Valor inválido.")
                sleep(1)
                continue

        if idade == "00":  # Sai do programa
            break

        # Lista de Perguntas
        perg = [
            "Você avalia a diversidade no seu local de trabalho como positiva?: ",
            "Acredita que todos os funcionários têm igualdade de oportunidades e são tratados de forma justa?: ",
            "Sua organização oferece treinamentos de sensibilização à diversidade?: ",
            "Acredita que a sua organização promove a participação de grupos sub-representados em cargos de liderança?: ",
        ]

        # Estrutura de repetição de Perguntas e Respostas

        for i in range(len(perg)):
            while True:
                os.system("cls")
                print(perg[i])
                print("[1] - Sim [2] - Não [3] - Não sei responder")
                x = int(input("Digite o valor correspondente a sua resposta:"))

                if x in [1, 2, 3]:
                    respostas[f"R{i+1}"] = x
                    break  # Sai do loop while quando um valor válido é digitado
                else:
                    print("Valor inválido. Digite 1, 2 ou 3.")
                    sleep(1)

        # Armazenar as respostas na lista
        listaC.append(respostas)

        # Salvar as respostas
        print("Salvando respostas, carregando proximo conjunto de perguntas.")
        salvarcsv(listaC)
        listaC.clear()  # Limpar listaC para evitar acumulo de respostas repitidas.
        sleep(1)


def salvarcsv(respostas):
    with open("respostas.csv", mode="a", newline="") as file:
        # Modo "a" serve para adicionar
        fieldnames = ["Idade", "Genero", "R1", "R2", "R3", "R4"]  # Cabeçalho
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            # Se o arquivo não existir, escreva a linha de separação "sep=,"
            file.write("sep=,\n")
            # Em seguida, escreva o cabeçalho
            writer.writeheader()
        writer.writerows(respostas)


def apresentacao():
    print("**Pesquisa sobre Diversidade no Local de Trabalho**\n")
    sleep(3)
    os.system("cls")

    print("Bem-vindo à nossa pesquisa sobre diversidade no local de trabalho!")
    sleep(2)

    print(
        "Estamos empenhados em promover um ambiente de trabalho inclusivo e igualitário para todos os nossos colaboradores."
    )
    sleep(3)

    print(
        "Esta pesquisa tem como objetivo coletar opiniões e percepções sobre a diversidade e inclusão em nossa organização."
    )
    sleep(4)

    print(
        "Suas respostas são extremamente valiosas e nos ajudarão a tomar medidas para melhorar nossa cultura empresarial.\n"
    )
    sleep(4)


apresentacao()
coletar_info()

print("Obrigado por usar nosso Quiz.")
print("Respostas salvas no arquivo 'respostas.csv'.")
