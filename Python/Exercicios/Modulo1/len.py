def test():
    x ="Isto é uma String"

    print(len(x))#17


    for i in range (len(x)):
        print(x[i])
        print(f"{x}[{i}]")

    for y in x:
        print(y)

def test2():
    x = "Banana", "Maça"

    print(len(x))#2

    for i in range (len(x)):
        print(x[i])

    for y in x:
        print(y)

def test3():
    x = "1234567890"

    print(x[8:]) #Copia apartir do 8 caracter
    print(x[:8]) #Copia até o 8 caracter

def test4():
    x = "1234567890"

    print(x[::-1])

    #x = "Gabriel"

    for i in range (len(x) -1, -1,-1): #Primeiro -1 vai para o ultimo indice no caso "0", o segundo se eu botasse 0 ele iria ate o 1, so que como e range ele vai ignora-la, então por isso vamos até o "0"
        print(x[i])


test4()