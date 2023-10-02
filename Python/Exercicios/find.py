def test1():
    x = "xxxxx:0.8475"

    i = x.find(":")
    y = x[i + 1:]

    n1 = float(y)*100

    print(n1)

def test2():
    x = "xxxxx:0.8475"

    y = x.split(":")


    n1 = float(y[1])*100

    print(n1)


