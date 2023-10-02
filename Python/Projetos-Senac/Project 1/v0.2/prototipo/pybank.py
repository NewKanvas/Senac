from login import banco
from conta import conta
from emprestimo import menuEmp
from transferencia import mtranf

# Usuario exemplo:
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
v = [0, 0, 0]

banco(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn)
