"""1. A função deve devolver um dicionário contendo o nome de um artista e o título
de um álbum.
2. Use a função para criar três dicionários que representem álbuns diferentes.
3. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Em grupos de 3 a 4 pessoas."""

def musical(y):

    x = ["1.Pop",
    "2.Metalica",
    "3.Rock"]

    print(x[y])

print("\n[1]-Pop")
y = int(input("Digite o album:"))
musical(y-1)

