from menu import menu

"""# Usuario exemplo:
contas = ["joão", "douglas"]
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 0]
fatura = [600, 600]
#i = 0

moedas = ["NitCoin", "Elitium", "NyanCoin"]
valorM = [4.53, 20.83, 10.03]
valorIn = [[200, 0, 0],  # 1
           [0, 0, 0]]    # 2

sorte = [1, -1, 1]
v = [0, 0, 0]"""


def ind(y, lista):
    for i in range(len(lista)):
        if lista[i] == y:
            return i
    return -1


def signup(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn):
    while True:
        print("--------------------\n-----Entrar------\n--------------------\n")
        print("Informe seus dados de login.\nDigite [0] para sair")

        x = input("Digite seu nome:")

        # Verificar se x está na lista de contas, mudar o índice para a posição da conta
        if x == "0":
            break

        if x.lower() in contas:
            i = ind(x, contas)
            x = input("Digite sua senha:")

            if x == senhas[i]:
                print("Senha correta")
                print(f"Seja bem-vindo {contas[i]}")
                menu(i, saldo, fatura, valorM, sorte, v, renda, contas, moedas, valorIn)
            else:
                print("Senha Incorreta")
        else:
            print("Login Incorreto")


def CriarConta(contas,senhas,saldo,fatura,renda,valorIn):
    x = input("Digite o nome de usuário:")

    if x in contas:
        print("Usuário já está em uso.")
    else:
        y = input("Digite a senha:")
        z = input("Digite a senha novamente:")
        if y == z:
            c = float(input("Digite sua renda:"))
            contas.append(x.lower())
            senhas.append(y)
            saldo.append(1000)
            renda.append(c)
            fatura.append(0)
            valorIn.append([0, 0, 0])
            print("Sua conta foi criada com sucesso\nVocê recebeu R$1000 por ter criado uma conta.")

        else:
            print("Senha incorreta")


def banco(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn):
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print(
            "[1] - Entrar\n[2] - Criar Conta\n[0] - Sair\n"
        )

        x = input("Selecione uma opção:")

        if x == "0":
            print("Saindo...")
            break
        elif x == "1":
            signup(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn)
        elif x == "2":
            CriarConta(contas,senhas,saldo,fatura,renda,valorIn)
        else:
            print("Opção inválida. Tente novamente.")


