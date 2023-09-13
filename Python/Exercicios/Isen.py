def ise():
    x = int(input("Digite seu Salario:"))
    y = 0

    if x < 600:
        print("Isento")

    elif x <= 1200:
        y = (x*(20/100))
        print (y)

    elif x >= 1200 and x <= 2000:
        y = (x*(25/100))
        print (y)
    elif x > 2000:
        y = (x*(30/100))
        print(y)

def mn():
    x = 1
    y = 2
    z = 3

    maior = max(x,y,z)

    print (maior)

def falha():
    x = "Banana"

    y = x.upper()
    print(y)

    def vogal(y):
        vog = "AEIOU"
        if y  in vog:
            print(f"{y} é vogal")
        else:
            print(f"{y} não é vogal")

    vogal(y)

    def eh_vogal(caractere):
        vogais = "aeiouAEIOU"
        if caractere in vogais:
            return True
        else:
            return False

    letra = "c"

    resultado = eh_vogal(letra)
    print(resultado)

def fatorial():
    x = 8
    y = x
    for x in range (1,x+1,1):
        # 8*7*6...
        # x = 8
        # x = x-1
        print(y)
        print(x)

fatorial()