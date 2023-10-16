import csv  # Adicione esta linha para importar o módulo csv

# Apresentação da pesquisa
print('Pesquisa sobre Diversidade no Local de Trabalho')
print()
print('Bem-vindo à nossa pesquisa sobre diversidade no local de trabalho! Estamos comprometidos em promover um ambiente de trabalho inclusivo e igualitário para todos os nossos colaboradores. Esta pesquisa visa coletar opiniões e percepções sobre a diversidade e inclusão na nossa organização. Suas respostas são extremamente valiosas e nos ajudarão a tomar medidas para melhorar nossa cultura empresarial.')
print()


# Coletando informações de cadastro
print('Por favor, forneça as seguintes informações de cadastro:')
idade = input('Qual sua idade? ')
print()
genero = input('Qual seu gênero? ')

# Crie uma lista para armazenar as respostas de cadastro
cadastro = [idade, genero]

# Instruções para responder a pesquisa
print('Nas perguntas a seguir, você poderá responder com:')
print('1: Sim')
print('2: Não')
print('3: Não sei responder')
print()


# Defina as perguntas
perguntas = [
    "Você avalia a diversidade no seu local de trabalho como positiva?: ",
    "Acredita que todos os funcionários têm igualdade de oportunidades e são tratados de forma justa?: ",
    "Sua organização oferece treinamentos de sensibilização à diversidade?: ",
    "Acredita que a sua organização promove a participação de grupos sub-representados em cargos de liderança?: "
]

# Crie uma lista para armazenar as respostas
respostas = []

# Peça aos participantes para responder às perguntas
for pergunta in perguntas:
    resposta = input(pergunta + " (1 a 3): ")
    # Valide a resposta se necessário
    respostas.append(int(resposta))  # Converter a resposta em um número inteiro
    print()  # Adicione uma linha em branco entre as perguntas

# Nome do arquivo CSV de saída
nome_arquivo = "respostas_pesquisa_diversidade.csv"

# Escreva as respostas no arquivo CSV
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["Pergunta", "Resposta"])  # Escreva o cabeçalho

    for i in range(len(perguntas)):
        escritor_csv.writerow([perguntas[i], respostas[i]])

print()
print(f"As respostas da pesquisa foram salvas em '{nome_arquivo}'.")