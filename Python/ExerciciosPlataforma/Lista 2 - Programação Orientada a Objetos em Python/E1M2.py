"""
O que é para fazer:

Crie uma fila de espera com os nomes de cinco pessoas e execute as seguintes operações: <ul><li>1-Imprima na tela a fila atual.</li><li>2-Remova o primeiro elemento da fila e imprima na tela a fila atualizada.</li><li>3-Adicione mais dois nomes à fila e imprima na tela a fila atualizada.</li></ul>

Como Fazer:

    Crie uma lista com cinco nomes de pessoas, que representará a fila de espera;
    Utilize a função print() para imprimir na tela a fila atual;
    Utilize o método pop(0) para remover o primeiro elemento da lista;
    Utilize novamente a função print() para imprimir a fila atualizada;
    Utilize o método append() para adicionar dois novos nomes à lista;
    Novamente, utilize a função print() para imprimir a fila atualizada.
"""

x = ["J", "O", "N", "A", "S"]

print(x)

x.pop(0)

print(x)

x.append("I")
x.append("O")

print(x)
