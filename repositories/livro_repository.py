from database_config_sqlalchemy import session
from models.livro import Livro

class LivroRepository:
    @staticmethod
    def criar_livro(livro):
        session.add(livro)
        session.commit()
    @staticmethod
    def listar_livros():
        return session.query(Livro).all()
    @staticmethod
    def listar_livros_disponiveis():
        session.query(Livro).filter(Livro.estoque > 0).all()
    @staticmethod
    def buscar_por_id(id):
        return session.get(Livro, id)
    @staticmethod
    def buscar_por_titulo(titulo):
        session.query(Livro).filter(Livro.titulo == titulo).first()
    @staticmethod
    def buscar_por_isbn(isbn):
        session.query(Livro).filter(Livro.isbn == isbn).first()
    @staticmethod
    def atualizar_livro():
        session.commit()