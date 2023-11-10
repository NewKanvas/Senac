lista = [1, -1, 1]
lista2 = [0, 0, 0]


def r():
    z = 0

    for _ in range(len(lista)):
        if lista[z] >= 1:
            # Vai para -1
            lista2[z] = 0

        elif lista[z] <= -1:
            # Vai para 1
            lista2[z] = 1

        if lista2[z] == 1:
            lista[z] += 0.2

        elif lista2[z] == 0:
            lista[z] -= 0.1

        z += 1


while True:
    r()

    print(f"{lista} \n {lista2}")

    x = input("Digite 0 para parar ou qualquer outra tecla para continuar: ")
    if x == "0":
        break
