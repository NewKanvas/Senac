def m1():
    def verifica(x):
        if x>=18:
            return "Já pode dirigir ou beber"
        else:
            return "Não pode nem dirigir nem beber"


    x = int(input("Digite sua idade:"))
    print(verifica(x))
#m1()

def previsaoRodagem(x,y):
    return y/x
    

x = int(input("Digite a quantidade de litros de gasolina no tanque do carro:"))
y = int(input("Digite  a quilometragem média por litro:"))
print(f"Você pode rodar{previsaoRodagem(x,y)}")