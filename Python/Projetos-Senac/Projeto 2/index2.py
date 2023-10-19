import csv
from time import sleep
import os


class Candidato:
    def __init__(self, idade, genero, r1, r2, r3, r4):
        self.idade = int(idade)
        self.genero = str(genero)
        self.r1 = str(r1)
        self.r2 = str(r2)
        self.r3 = str(r3)
        self.r4 = str(r4)

    def salvar(self):
        with open("respostas.csv", mode="a", newline="") as file:
            # Modo "a" serve para adicionar
            fieldnames = ["Idade", "Genero", "R1", "R2", "R3", "R4"]  # Cabeçalho
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Se o arquivo não existir,
            if file.tell() == 0:
                # Escreva a linha de separação "sep=,"
                file.write("sep=,\n")
                # Em seguida, escreva o cabeçalho
                writer.writeheader()

            writer.writerow(
                {
                    "Idade": self.idade,
                    "Genero": self.genero,
                    "R1": self.r1,
                    "R2": self.r2,
                    "R3": self.r3,
                    "R4": self.r4,
                }
            )
        # Resposta de Salmento
        print(
            "Respostas foram salvas no arquivo 'respostas.csv', carregando proximo conjunto de perguntas."
        )
        sleep(1)


# Pergunta da Idade
def idade(respostas):
    while True:
        os.system("cls")

        idade = input("Identifique sua idade (ou '00' para sair): ")

        if idade == "00":  # Sai de dentro do loop
            print("Obrigado por usar nosso Quiz.")
            print("Respostas salvas no arquivo 'respostas.csv'.")
            exit()

        idade = int(idade)

        if idade > 0:
            respostas["Idade"] = idade
            break

        else:
            print("Valor inválido.")
            sleep(1)
            continue


# Perguntar Genero
def genero(respostas):
    while True:
        os.system("cls")

        print("Identifique seu gênero.")
        print("[1] - Masculino [2] - Feminino [3] - Não Binário")

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
            print("Opção inválida. Tente novamente.")
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
            print("[1] - Sim [2] - Não [3] - Não sei responder")
            x = int(input("Digite o valor correspondente a sua resposta:"))

            if x in [1, 2, 3]:
                respostas[f"R{i+1}"] = x
                break  # Sai do loop while quando um valor válido é digitado
            else:
                print("Valor inválido. Digite 1, 2 ou 3.")
                sleep(1)


# iniciar Classe
def iniciar():
    while True:
        respostas = {}
        idade(respostas)
        genero(respostas)
        perguntas(respostas)
        p = Candidato(
            respostas["Idade"],
            respostas["Genero"],
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
    sleep(3)

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
