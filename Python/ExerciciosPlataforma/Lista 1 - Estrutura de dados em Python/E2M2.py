"""
O que é para fazer:

Crie duas listas de tamanho igual com valores numéricos de sua escolha. Crie uma nova lista que seja a fusão das duas primeiras, de forma que os elementos sejam intercalados. Por fim, imprima a nova lista na tela.

Como Fazer:

    Crie duas listas de tamanho igual com valores numéricos de sua escolha;
    Crie uma nova lista vazia para armazenar a fusão das duas primeiras;
    Utilize um laço de repetição para percorrer todos os índices das listas originais;
    Para cada índice, adicione o elemento da primeira lista na nova lista e, em seguida, adicione o elemento correspondente da segunda lista na nova lista;
    Se as listas originais possuem tamanhos diferentes, adicione os elementos restantes da lista maior no final da nova lista;
    Imprima a nova lista na tela.
"""


l1 = [1, 2, 3]
l2 = [4, 5, 6, 4, 4]

lc = []

for i in range(len(l1)):
    lc.append(l1[i])
    lc.append(l2[i])

if len(l1) > len(l2):
    lc.append(l1[len(l2) :])  # Usar extend...
elif len(l2) > len(l1):
    lc.append(l2[len(l1) :])

elif len(l2) == len(l1):
    pass

print(lc)
