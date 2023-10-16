opçoes = {
    1: "primeiro",
    2: "segundo",
    3: "terceiro"
}

x = int(input("Digite um numero:"))

if x in opçoes:
    print(opçoes[x])