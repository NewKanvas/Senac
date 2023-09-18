#temp = int(input("Insira a sua temperatura:")) O problema principal está aqui, se voce receber a string e converter ela para um numero vai dar erro
#while temp != "SAIR" : 
#    if temp >= 38 and temp <= 39 :
#        print("Você está com febre. Tome um remédio e repouse")
#        temp = int(input("Insira a sua temperatura:"))
#    elif temp > 39:
#        print("Você está com febre. Tome um remédio, procure um médico.")
#        temp = int(input("Insira a sua temperatura:"))
#    elif int(temp) < 38:
#        print("Nada de febre")
#        temp = int(input("Insira a sua temperatura:"))
#else :
#    print("Finalizando programa.")

def a():
    #Criar um loop
    while True:
        #Fazer pergunta
        temp = input("Insira a sua temperatura:")

        #Checar se o input e "sair"
        if temp == "sair":
            print("Saindo")
            break
        
        else:
            temp = int(temp)

        #Verificação
        if temp >= 38 and temp <= 39 :
            print("Você está com febre. Tome um remédio e repouse")

        elif temp > 39:
            print("Você está com febre. Tome um remédio, procure um médico.")

        # elif temp < 38: não e preciso.
        else:
            print("Nada de febre")

def b():
    temp = input("Insira a sua temperatura:") #O problema principal está aqui, se voce receber a string e converter ela para um numero vai dar erro

    while temp != "SAIR" : #Se temp for diferente de SAIR, ou seja um numero, isso vai gerar um problema.

        temp = int(temp) #Converte o temp para um numero

        if temp >= 38 and temp <= 39 :
            print("Você está com febre. Tome um remédio e repouse")
            
        elif temp > 39:
            print("Você está com febre. Tome um remédio, procure um médico.")
            
        else:
            print("Nada de febre")
