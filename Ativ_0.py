import os

class Livro:
    livros = []

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @classmethod

    def listar_livros(cls):
        os.system('cls')
        print(f'\n{'Titulo do livro'.ljust(25)} | {'Autor do livro'.ljust(25)} | {'Páginas do livro'.ljust(25)} \n')
        for lista_livros in cls.livros:
            print(f'{lista_livros.titulo.ljust(25)} | {lista_livros.autor.ljust(25)} | {lista_livros.paginas.ljust(25)} ')

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

livro_01 = Livro('Praça', 'Gourmet', '150')
livro_02 = Livro('Praça', 'Gourmet', '150')
livro_03 = Livro('Praça', 'Gourmet', '150')

Livro.listar_livros()

#----------



