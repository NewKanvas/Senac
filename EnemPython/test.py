lista = {"Porcentagem": "a", "Media": "b", "Logaritimo": "c"}

x = 0

if x < 0:
    x = len(lista) - 1
elif x >= len(lista):
    x = 0

for i, op in enumerate(lista):
    if x == i:
        print(f">> [{i+1}] {op}")
    else:
        print(f"[{i+1}] {op}")
