"""
Atividade: Senta que lá vem a história
➔ O QUE FAZER?
1. Criar uma classe Livro (atributos Título e ISBN);
2. Criar uma classe Ebook (atributo Link para Download);
3. Fazer com que a classe Ebook herde a Classe Livro;
4. Demonstrar o funcionamento da herança.
"""


class Livro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def dados(self):
        print(f"Título: {self.titulo}\nISBN: {self.isbn}\n")


class Ebook(Livro):
    def __init__(
        self,
        titulo,
        isbn,
        link,
        download,
    ):
        super().__init__(titulo, isbn)
        self.link = link
        self.download = download

    def dados(self):
        print(
            f"Título: {self.titulo}\nISBN: {self.isbn}\nLink: {self.link}\Download: {self.download}\n"
        )


livro1 = Livro("Yuri o Grande", 12313)
livro1.dados()

livro2 = Ebook("Myamoto", 2423, "link", "link2")
livro2.dados()
