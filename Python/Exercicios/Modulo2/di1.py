d = {
    "fruta": "banana",
    "numero": "um",
    "objeto": "tesoura",
    "adjetivo": "belo",
    "criatura": "humano",
}

print("")
print(d.keys())

x = input("Digite uma chave do dicionario:")

if x in d:
    print(d.get(x))
else:
    print("Palavra não esta no dicionario")
