"""
O que é para fazer:

Crie uma tupla com 5 elementos e realize as seguintes operações: <ul><li>1-Imprima na tela o tamanho da tupla;</li><li>2-Crie uma nova tupla que contenha os elementos da tupla original em ordem reversa;</li><li>3-Imprima na tela os elementos da nova tupla separados por ""-"".</li></ul>

Como Fazer:

    Crie uma tupla com 5 elementos de sua escolha;
    Utilize a função len() para imprimir na tela o tamanho da tupla;
    Crie uma nova tupla que contenha os elementos da tupla original em ordem reversa, utilizando o fatiamento com parâmetro -1;
    Utilize o método join() para imprimir na tela os elementos da nova tupla, separados por ""-"".

"""

x = (1, 2, 3, 4, 5)

print(len(x))

y = x[::-1]

"""for i in range(len(x) - 1, -1, -1):
    y += (x[i],)"""

print(y)

# y = str(y)

print("-".join(map(str, y)))
