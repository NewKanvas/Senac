# lista de dicionários
carro01 = {"cor": "preto", "motor": 2.0, "ano": 2012}
carro02 = {"cor": "branco", "motor": 1.0, "ano": 2013}
carro03 = {"cor": "prata", "motor": 2.4, "ano": 2014}
carro04 = {"cor": "vermelho", "motor": 1.6, "ano": 2015}


# declarando dicionário de dicionários
dic_carros = {"Gol": carro01, "Corsa": carro02, "Hilux": carro03, "Fiesta": carro04}
# iterando sobre dicionário de dicionários
for key in dic_carros:
    print(dic_carros[key])
