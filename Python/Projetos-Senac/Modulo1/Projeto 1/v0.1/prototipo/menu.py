# from login import singup
from conta import conta
from emprestimo import menuEmp
from transferencia import mtranfsel
from suporte import suporte
from investimento import minvest

'''# Usuario exemplo:
contas = ["João", "Douglas"]
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 0]
fatura = [600, 600]
i = 0

moedas = ["NitCoin", "Elitium", "NyanCoin"]
valorM = [4.53, 20.83, 10.03]
valorIn = [0, 0, 0]


sorte = [1, -1, 1]
v = [0, 0, 0]'''


def menu(i,saldo,fatura,valorM,sorte,v,renda,contas,moedas,valorIn):
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print(
            "[1] - Conta\n[2] - Emprestimo \n[3] - Transferencia\n[4] - Investimentos \n[5] - Suporte \n[0] - Sair\n"
        )

        x = int(input("Digite um numero:"))

        if x == 1:
            print("[Conta] Selecionada")
            conta(saldo, i, fatura, valorM, sorte, v)
        elif x == 2:
            print("[Emprestimo] Selecionado")
            menuEmp(saldo, i, fatura, renda)
        elif x == 3:
            print("[Transferencia] Selecionado")
            mtranfsel(contas, saldo, i)
        elif x == 4:
            minvest(saldo, i, moedas, valorM, valorIn, sorte)
        elif x == 5:
            suporte()

        elif x == 0:
            print("Saindo...\n")
            break
        else:
            print("Opção Invalida")


#menu(i)

# Criar um processo de login ou criação de conta(Iniciar a conta com R$100 ou algo assim para conseguir experimentar os menus)
