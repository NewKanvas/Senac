def lucro():
    x =float(input("Digite Valor:"))

    if (x<20):
        y = x*(45/100)
        print(y+x)
    else:
        y = x*(30/100)
        print(y+x)

def somando():
    x =int(input("Digite a quantidade de números que serão somados:"))
    y = 0

    for x in range (0,x,1):
        z = int(input(f"[{x+1}] - Digite um numero:"))
        y = y+z
        print(y)

def divisores():
    x = 0

    for x in range (2000, 3200,1):
        if (x%7==0):
            if (x%5 != 0):
                print (x)

#def imc():

x = int(input("Digite o numero de pacientes:"))

for x in range (0,x,1):
    z = (input("Digite o nome do paciente:"))
    y = float(input("Digite a altura do paciente"))
    c = float(input("Digite o peso do paciente"))

    imc = c /(y**2)
    print(f"O {z}, tem {y} de altura, pesa {c} tem o imc igual a {imc}")