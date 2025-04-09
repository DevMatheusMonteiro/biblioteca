from database_config_sqlalchemy import session
from models.livro import Livro
from models.emprestimo import Emprestimo

class LivroRepository:
    @staticmethod
    def adicionar(livro):
        session.add(livro)
        session.commit()
    @staticmethod
    def listar_todos():
        return session.query(Livro).all()
    @staticmethod
    def buscar_por_id(livro_id):
        return session.get(Livro, livro_id)
    @staticmethod
    def contar_emprestados(livro_id):
        return session.query(Emprestimo).filter_by(livro_id=livro_id, data_devolucao=None).count()