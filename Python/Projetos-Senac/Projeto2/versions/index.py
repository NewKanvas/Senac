"""
CONTEXTO:

Sua equipe recebeu uma nova solicitação de projeto! Dessa vez
para desenvolver uma pesquisa digital com a população de
várias cidades do Brasil.
Para isso, será necessário armazenar os dados dessa pesquisa
em um arquivo .csv para utilização em análises futuras.
A pesquisa será feita a partir de um levantamento ativo, realizado
pelos funcionários da empresa que irão sair com o projeto nas ruas
para coletar as respostas.


O QUE É PARA FAZER?

Você e seu squad devem desenvolver um projeto capaz de
armazenar dados recolhidos na pesquisa em um documento csv.
As perguntas para essa pesquisa (assim como o tema dela) devem
ser definidas pelo grupo.


REQUISITOS
■ A entrada dos dados deverá ser realizada pelo teclado utilizando estruturas de repetição;
■ Estruturas condicionais e de repetição devem ser utilizadas;
■ Estruturas de dados devem ser utilizadas (listas, pilhas, filas ou dicionários), quando for
possível o uso;
■ Deverá ser utilizada a estrutura de funções, quando for possível o uso;
■ Deve ser utilizado o paradigma de orientação a objetos;
■ O projeto desenvolvido deverá ser disponibilizado em repositório no GitHub;
■ O projeto desenvolvido deverá estar funcional, ou seja, caso seja necessário algum teste
durante a apresentação ou correção do trabalho, ele deve estar funcionando normalmente.
■ Seu projeto precisa possuir uma evidência de entrega no arquivo README.md, ou seja,
um pequeno parágrafo com uma explicação do que foi feito no projeto e a defesa das
escolhas feitas.
■ O projeto deve ser apresentado em grupo e:
● Todos os integrantes do grupo deverão apresentar;
● Utilizar slides de apoio para a apresentação;
● Seu grupo terá 15 minutos (no máximo) para apresentar


COMO FAZER?

Detalhes do projeto:
⇨ A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as
questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3).

⇨ Para iniciar o questionário, será solicitado ao usuário que informe a sua idade e gênero. Cada
linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3,
resposta_4, data e hora da resposta.

⇨ O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as
respostas informadas nas linhas do .csv até que a idade de 00 seja informada; então, podemos
ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada
o projeto para de executar).

⇨ Com os dados preenchidos no .csv, o grupo deve realizar uma exibição simples dos resultados
utilizando o Excel (com uma simulação de 10 respostas no questionário para gerar os dados). Na
apresentação, deverão ser demonstrados o funcionamento do questionário e o exemplo dos
dados coletados.

"""

from time import sleep
import os


listaC = []  # Lista de dicionarios


def perguntasInicio(i):
    respostas = {}  # Dicionario para as respostas.

    # Pergunta de Genero

    os.system("cls")
    print("Identifique seu gênero.")
    print("[1] - Masculino [2] - Feminino [3] - Não Binário")
    x = int(input("Digite o número correspondente ao seu gênero:"))

    # Transformação da respotas de Genero

    if x == 1:
        respostas["Genero"] = "M"
    elif x == 2:
        respostas["Genero"] = "F"
    elif x == 3:
        respostas["Genero"] = "NB"

    # Pergunta da Idade

    os.system("cls")
    print("Identifique sua idade:")
    print("(Digite '00' para sair)")
    y = input("Digite sua idade:")

    if y == "00":
        os.system("cls")
        print(listaC)
        exit()
    else:
        respostas["Idade"] = y

    perguntasQuiz(i, respostas)


def perguntasQuiz(i, respostas):
    # Lista de Perguntas
    perg = [
        "Pergunta 1",
        "Pergunta 2",
        "Pergunta 3",
        "Pergunta 4",
    ]

    # Estrutura de repetição de Perguntas e Respostas

    for i in range(len(perg)):
        os.system("cls")
        print(perg[i])
        print("[1] - Sim [2] - Não [3] - Não sei responder")
        x = int(input("Digite o valor correspondente a sua resposta:"))

        respostas[f"R{i+1}"] = x

    listaC.append(respostas)  # Armazenar a lista de respostas como dicionario na ListaC

    # Mensagem de Despedida:

    os.system("cls")
    print("Obrigado por responder.\nCarregando proximo Quiz.")
    sleep(2)


i = 0
while True:
    perguntasInicio(i)
    i += 1
