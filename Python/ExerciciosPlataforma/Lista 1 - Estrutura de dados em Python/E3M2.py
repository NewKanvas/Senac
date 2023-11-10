"""
Como Fazer:

    Crie uma lista com 5 números inteiros de sua escolha;
    Declare uma variável para armazenar a soma dos valores da lista;
    Utilize um laço de repetição para percorrer todos os elementos da lista e ir somando seus valores na variável criada no passo anterior;
    Imprima o resultado da soma na tela.
"""

x = [1, 2, 3, 4, 5]

z = 0

for i in range(len(x)):
    z = z + x[i]

print(z)
