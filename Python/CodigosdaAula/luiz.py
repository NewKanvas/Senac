month = int(input("Digite:"))

meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#print(meses[1])

#print(meses[month-1])

if month >=1 and month <=12:
    nome_mes = meses[month - 1]
    print(nome_mes)
else:
    print("Valor fora do intervalo válido")