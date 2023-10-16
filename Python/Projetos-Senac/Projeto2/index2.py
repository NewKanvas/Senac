import csv
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
            continue

        # Pergunta da Idade

        idade = input("Identifique sua idade (ou '00' para sair): ")

        if idade == "00":
            break

        respostas["Idade"] = idade

        # Lista de Perguntas
        perg = [
            "Pergunta 1",
            "Pergunta 2",
            "Pergunta 3",
            "Pergunta 4",
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
        listaC.clear() #Limpar listaC para evitar acumulo de respostas repitidas.
        sleep(1)


def salvarcsv(respostas):
    with open("respostas.csv", mode="a", newline="") as file:
        # Modo "a" serve para adicionar
        fieldnames = ["Idade", "Genero", "R1", "R2", "R3", "R4"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            # Se o arquivo não existir, escreva o cabeçalho
            writer.writeheader()
        writer.writerows(respostas)


coletar_info()
print("Obrigado por usar nosso Quiz.")
print("Respostas salvas no arquivo 'respostas.csv'.")
