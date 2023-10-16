"""
Atividade: Criando um aninhamento
➔ O QUE FAZER?
Criar um catálogo de cidades:
1.Elabore um algoritmo que cria uma lista de
dicionários de cidades em que as chaves são o
nome da cidade e o estado a que ela pertence.
2. Armazene a população, se há praia, região
em que está inserida e o gentílico da cidade (ex:
paulista, carioca, recifense, etc...).
3. Apresente o nome de cada cidade e todas as
informações que você armazenou sobre ela.
"""

listaCidade = [
    {
        "cidade": "Rio de Janeiro",
        "estado": "Rio de janeiro",
        "população": 1000,
        "praia": True,
        "gentilico": "Carioca",
    },
]

z = {}

listaKeys = (
    "cidade",  # 0
    "estado",  # 1
    "população",  # 2
    "praia",  # 3
    "gentilico",  # 4
)

listaPergunta = (
    "Digite o nome da cidade:",
    "Digite o estado da cidade:",
    "Digite a população:",
    "Tem praia[S/N]:",
    "Digite o gentílico:",
)

while True:
    for i in range(len(listaPergunta)):
        x = input(listaPergunta[i])
        z[listaKeys[i]] = x

    listaCidade.append(z)
    for cidade in listaCidade:
        print(
            f"Nome da cidade: {cidade['cidade']};\n Estado: {cidade['estado']};\n População: {cidade['população']};\n Tem praia: {'Sim' if cidade['praia'] else 'Não'}, Gentílico: {cidade['gentilico']}\n"
        )
