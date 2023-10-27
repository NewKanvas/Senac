import csv
from datetime import datetime
from time import sleep
import os
from cores import *


class Candidato:
    def __init__(self, idade, genero, estado, r1, r2, r3, r4):
        self.idade = int(idade)
        self.genero = str(genero)
        self.estado = str(estado)
        self.r1 = str(r1)
        self.r2 = str(r2)
        self.r3 = str(r3)
        self.r4 = str(r4)

    def salvar(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        csvfilename = os.path.join(dirname, "respostas.csv")

        with open(csvfilename, mode="a", newline="", encoding="utf-8") as file:
            # Modo "a" serve para adicionar
            fieldnames = [
                "Idade",
                "Genero",
                "Estado",
                "R1",
                "R2",
                "R3",
                "R4",
                "Date",
            ]  # Cabeçalho
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Se o arquivo não existir,
            if file.tell() == 0:
                # Escreva a linha de separação "sep=,"
                file.write("sep=,\n")
                # Em seguida, escreva o cabeçalho
                writer.writeheader()

            now = datetime.now()
            date = now.strftime("%d-%m-%Y %H:%M:%S")

            writer.writerow(
                {
                    "Idade": self.idade,
                    "Genero": self.genero,
                    "Estado": self.estado,
                    "R1": self.r1,
                    "R2": self.r2,
                    "R3": self.r3,
                    "R4": self.r4,
                    "Date": date,
                }
            )
        # Resposta de Salvamento
        print(
            f"{g}Respostas foram salvas no arquivo {y}'respostas.csv'{g}, carregando próximo conjunto de perguntas.{rt}"
        )

        sleep(2)


# Pergunta da Idade
def idade(respostas):
    while True:
        os.system("cls")

        idade = input(f"Identifique sua idade {y}(ou '00' para sair): {rt}")

        if idade == "00":
            print(f"{g}Obrigado por usar nosso Quiz.{rt}")
            print(f"{g}Respostas foram salvas no arquivo {y}'respostas.csv'.{rt}")
            exit()
        idade = int(idade)
        if idade > 0:
            respostas["Idade"] = idade
            break
        else:
            print(f"{r}Valor inválido.{rt}")
            sleep(1)
            continue


# Perguntar Genero
def genero(respostas):
    while True:
        os.system("cls")

        print("Identifique seu gênero.")
        print(f"{y}[1]{rt} - Masculino {y}[2]{rt} - Feminino {y}[3]{rt} - Não Binário")

        genero = int(input("Digite o número correspondente ao seu gênero: "))

        # Transformação da respotas de Genero

        if genero == 1:
            respostas["Genero"] = "M"
            break
        elif genero == 2:
            respostas["Genero"] = "F"
            break
        elif genero == 3:
            respostas["Genero"] = "NB"
            break

        else:
            print(f"{r}Opção inválida. Tente novamente.{rt}")
            sleep(1)
            continue


# Perguntas
def perguntas(respostas):
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
            print(f"{i+1}) - {perg[i]}")

            # Selecioanar a melhor opção de cor
            """
            print(f"{y}[1]{rt} - Sim {y}[2]{rt} - Não {y}[3]{rt} - Não sei responder")
            print(f"{g}[1] - Sim{rt} {r}[2] - Não{rt} {b}[3] - Não sei responder{rt}")
            print(
                f"{y}[1]{rt} - {g}Sim{rt} {y}[2]{rt} - {r}Não{rt} {y}[3]{rt} - {b}Não sei responder{rt}"
            )
            """

            print(
                f"{g}[1] - Sim{rt}\n{r}[2] - Não{rt}\n[3] - Não sei responder",
            )

            x = int(input("Digite o valor correspondente a sua resposta:"))

            if x in [1, 2, 3]:
                respostas[f"R{i+1}"] = x
                break  # Sai do loop while quando um valor válido é digitado
            else:
                print(f"{r}Valor inválido. Digite 1, 2 ou 3.{rt}")
                sleep(1)


# Estados
def estado(respostas):
    while True:
        os.system("cls")
        # Lista de Estados
        est = {
            "Rio de Janeiro": "RJ",
            "São Paulo": "SP",
            "Minas Gerais": "MG",
            "Paraná": "PR",
            "Rio Grande do Sul": "RS",
            "Pará": "PA",
            "Bahia": "BA",
            "Santa Catarina": "SC",
            "Acre": "AC",
            "Ceará": "CE",
        }

        print("Identifique seu estado:")
        for i, estado in enumerate(est, start=1):
            print(f"{y}[{i}]{rt} - {g}{estado}{rt}")

        x = int(input("Digite o valor correspondente a sua resposta:"))

        if x > 0:
            estado_selecionado = list(est.values())[x - 1]
            respostas["Estado"] = estado_selecionado
            print(respostas)
            break

        else:
            print(f"{r}Opção inválida.{rt}")
            sleep(2)
