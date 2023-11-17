from time import sleep

# Biblioteca


def matematica():
    title = "Matematica"
    lista = {
        "Porcentagem": porcentagem,
        "Media": "media",
        "Logaritimo": "logaritimo",
    }
    return title, lista


# Assuntos


def porcentagem():
    title = "Porcentagem"
    texto = [
        "Porcentagem é uma forma de expressar uma parte de um todo em termos percentuais.\n\nMacete: Para calcular a porcentagem de um valor, multiplique o valor pela porcentagem e mova a vírgula duas posições para a frente.\nPor exemplo, 20 alunos representam 35%. 20 x 35 = 700.\nPortanto, 35% de 20 alunos são 7 alunas.",
        "Para encontrar a parte complementar (porcentagem restante),\nsubtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres,\n\n100% - 35% = 65% são homens.\n20 x 65 = 1300\n\nAssim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
        "Para encontrar o valor original de um numero com aumento em porcentagem.\n\n[Valor com aumento]/(100+x%)\n\nExemplo:\nSe um trabalhador tivesse 7% de aumento do seu salario atual receberia R$ 2.675,00.\n\n2675/(100+7)\n2675/107 = 2500\nValor do salario atual = 2500",
    ]

    return title, texto
