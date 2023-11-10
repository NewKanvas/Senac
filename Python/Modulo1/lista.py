x  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11,12,13,14,15]
y  = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def algo(x,y):
    xy =[]
    xpy = []
    


    i = 0
    for z in range(0,15,1):
        xy.append(x[i])
        xy.append(y[i])
        i = i+1

    print("\nLista de elementos no mesmo indice:")
    print(xy)

    i = 0
    for z in range(0,15,1):
        print(x[i],"+",y[i],"=",x[i]+y[i])

        xpy.append(x[i]+y[i])

        i = i+1

    print("\nLista de soma dos elementos de cada lista:")
    print(xpy)

    xny = []

    i= 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            xny.append(x[i])

    for i in range(len(y)):
        if y[i] % 2 == 0:
            xny.append(y[i])
        

    print("\nListas sem numeros impares:")
    print(xny)

algo(x,y)