x = 0
y = 0

def mudarValor(x,y):
    x = int(input("Digite o valor de X:"))
    y = int(input("Digite o valor de Y:"))

    return x,y

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "1"
    else:
        return x / y