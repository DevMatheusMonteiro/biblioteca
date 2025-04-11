from services.livro_service import LivroService
from app_error import AppError

class LivroController():
    @staticmethod
    def criar_livro(titulo, isbn, genero, data_publicacao, qtd_paginas, estoque):
        try:
            LivroService.criar_livro(titulo=titulo, isbn=isbn, genero=genero, data_publicacao=data_publicacao, qtd_paginas=qtd_paginas, estoque=estoque)
            return "Livro adicionado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def listar_livros():
        try:
            return LivroService.listar_livros()
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def listar_livros_disponiveis():
        try:
            return LivroService.listar_livros_disponiveis()
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def atualizar_livro(id, titulo, isbn, genero, data_publicacao, qtd_paginas, estoque):
        try:
            LivroService.atualizar_livro(id=id, titulo=titulo, isbn=isbn, genero=genero, data_publicacao=data_publicacao, qtd_paginas=qtd_paginas, estoque=estoque)
            return "Livro atualizado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."