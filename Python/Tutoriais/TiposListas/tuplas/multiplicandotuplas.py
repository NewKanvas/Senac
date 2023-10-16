x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

z = ()

for i in range(len(x)):
    z += (x[i] * y[i],)

print(z)

####

tupla_x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_y = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
tupla_z = tuple(
    x * y for x, y in zip(tupla_x, tupla_y)
)  # zip pega os elementos de cada lista e faz uma mini lista sendo (1,10) ae ele para cada x e y multiplicado x*y
print(tupla_z)
