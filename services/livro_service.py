from datetime import datetime
from models.livro import Livro
from repositories.livro_repository import LivroRepository
from app_error import AppError

class LivroService:
    @staticmethod
    def criar_livro(titulo, isbn, genero, data_publicacao, qtd_paginas, estoque):
        if titulo == None or titulo.strip() == "":
            raise AppError("Erro: título nulo ou vazio.")
        if isbn == None or isbn.strip() == "":
            raise AppError("Erro: isbn nulo ou vazio.")
        livro_por_titulo = LivroRepository.buscar_por_titulo(titulo)
        livro_por_isbn = LivroRepository.buscar_por_isbn(isbn)
        if livro_por_titulo or livro_por_isbn:
            raise AppError("Erro: livro já cadastrado.")
        if genero == None or genero.strip() == "":
            raise AppError("Erro: gênero nulo ou vazio.")
        if data_publicacao == None:
            raise AppError("Erro: data de publicação nula.")
        if qtd_paginas <= 0:
            raise AppError("Erro: quantidade de páginas menor ou igual a 0.")
        if estoque < 0:
            raise AppError("Erro: estoque menor que 0.")
        livro = Livro(titulo=titulo, isbn=isbn, genero=genero, data_publicacao=data_publicacao, qtd_paginas=qtd_paginas, estoque=estoque)
        LivroRepository.criar_livro(livro)
    @staticmethod
    def listar_livros():
        return LivroRepository.listar_livros()
    @staticmethod
    def listar_livros_disponiveis():
        return LivroRepository.listar_livros_disponiveis()
    @staticmethod
    def atualizar_livro(id, titulo=None, isbn=None, genero=None, data_publicacao=None, qtd_paginas=None, estoque=None):
        livro = LivroRepository.buscar_por_id(id)
        livro_por_titulo = LivroRepository.buscar_por_titulo(titulo)
        livro_por_isbn = LivroRepository.buscar_por_isbn(isbn)
        if (livro_por_titulo and livro_por_titulo.id != livro.id) or (livro_por_isbn and livro_por_isbn.id != livro.id):
            raise AppError("Erro: livro já cadastrado.")
        if qtd_paginas and qtd_paginas <= 0:
            raise AppError("Erro: quantidade de páginas menor ou igual a 0.")
        if estoque and estoque < 0:
            raise AppError("Erro: estoque menor que 0.")
        livro.titulo = titulo if titulo != None and titulo.strip() != "" else livro.titulo
        livro.isbn = isbn if isbn != None and isbn.strip() != "" else livro.isbn
        livro.genero = genero if genero != None and genero.strip() != "" else livro.genero
        livro.data_publicacao = data_publicacao if data_publicacao != None else livro.data_publicacao
        livro.qtd_paginas = qtd_paginas if qtd_paginas != None else livro.qtd_paginas
        livro.estoque = estoque if estoque != None else livro.estoque
        LivroRepository.atualizar_livro()