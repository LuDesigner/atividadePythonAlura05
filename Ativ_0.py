class Livro:
    livros = []

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)  # Garantir que páginas sejam armazenadas como inteiros
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @classmethod
    def listar_livros(cls):
        print(f'\n{"Titulo do livro".ljust(25)} | {"Autor do livro".ljust(25)} | {"Páginas do livro".ljust(25)}')
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {str(livro.paginas).ljust(25)}')

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        """Aumenta o número de páginas do livro."""
        self.paginas += quantidade

# Criando livros com a quantidade de páginas corretamente atribuída como inteiro
livro_01 = Livro('Praça', 'Gourmet', 150)
livro_02 = Livro('Praça', 'Gourmet', 150)
livro_03 = Livro('Praça', 'Gourmet', 150)

# Listando livros
Livro.listar_livros()