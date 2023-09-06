#TV
def tv():
    p = int(input("Digite as polegadas:"))
    c = float(input("Digite o valor:"))

    if p < 32 and c > 1900:
        print("Não Comprar")
    elif p >= 32 and c <= 1900:
        print("Comprar")
    else:
        print("Não Comprar")

def febre():       
    temp = float(input("Diga sua temperatura:"))

    if temp >= 38:
        print ("Está com febre.")
    else:
        print("Não está com febre")

