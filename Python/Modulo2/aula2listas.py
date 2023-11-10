"""x = [1, 2]
y = [3, 4]

z = x + y
print(z)

x = "Hello "
y = "World"

z = x + y
print(z)

x = 1
y = 2

z = x + y
print(z)
"""
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista3 = []

for x in range(0, len(lista1)):
    lista3.append(lista1[x] * lista2[x])

print(lista3)
